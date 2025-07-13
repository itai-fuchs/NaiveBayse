import os
from Clean_Table import Cleaner
from bayesian_model import BayesianModel
from testing_model import TestingModel
from classifier import BayesianClassifier


class UI:
    """
    Main user interface for loading data, building a model, testing, and prediction.
    """

    def __init__(self):
        """
        Initialize internal variables.
        """
        self.table = None
        self.model = None
        self.testModel = None

    def start(self):
        """
        Load CSV file from user input and build the Bayesian model.
        """
        print("---- Naive Bayesian Classifier ----")
        while True:
            path = input("Enter path to CSV file: ").strip('\'"')
            if not os.path.exists(path):
                print("File not found. Please try again.\n")
                continue
            try:
                self.table = Cleaner(path).table

                self.testModel=TestingModel(self.table)

                self.model = BayesianModel(self.testModel.model_table)
                print("File loaded and model built successfully.\n")
                break
            except Exception as e:
                print(f"Failed to load or process file: {e}")
                continue

        self.main_menu()

    def main_menu(self):
        """
        Display main menu for choosing actions: test model, make prediction, or exit.
        """
        while True:


            print("\nChoose an action:")
            print("1. Check model success rate")
            print("2. Enter values for prediction")
            print("3. Exit")

            choice = input().strip()

            match choice:
                case "1":
                    # Test the model using the test table
                    try:


                        self.testModel = TestingModel(self.testModel.model_table)
                        print(self.testModel.test())
                    except Exception as e:
                        print(f"Error while testing the model: {e}")

                case "2":
                    # Perform prediction using user input
                    try:
                        self.predict()
                    except Exception as e:
                        print(f"Error during prediction: {e}")

                case "3":
                    # Exit the program
                    print("Goodbye!")
                    break

                case _:
                    print("Invalid input. Please enter 1, 2, or 3.")

    def predict(self):
        """
        Collect user input for prediction and call the classifier.
        """
        user_input = {}
        print("\nEnter values for prediction:")

        for col in self.model.columns:
            try:
                unique_vals = list(self.model.table[col].dropna().unique())
                if not unique_vals:
                    raise ValueError(f"No unique values found for column '{col}'")

                print(f"\nAvailable values for '{col}':")
                for i, val in enumerate(unique_vals):
                    print(f"{i + 1}. {val}")

                index = input(f"Choose a number (1-{len(unique_vals)}): ").strip()
                while not index.isdigit() or not (1 <= int(index) <= len(unique_vals)):
                    index = input(f"Invalid. Choose a number (1-{len(unique_vals)}): ").strip()

                user_input[col] = unique_vals[int(index) - 1]

            except Exception as e:
                print(f"Error while collecting input for '{col}': {e}")
                return

        try:
            prediction = BayesianClassifier.prediction(
                user_input,
                self.model.model,
                self.model.ratio_target_variable
            )
            print(f"\nPrediction: {prediction}")
        except Exception as e:
            print(f"Failed to make prediction: {e}")




a=UI()
a.start()




