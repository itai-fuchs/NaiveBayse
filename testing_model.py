from classifier import BayesianClassifier
from bayesian_model import BayesianModel
from Clean_Table import Cleaner
class TestingModel:
    """
    Performs tests on the Bayesian model
    """

    def __init__(self, table):
        self.table = table
        self.model_table = None
        self.test_table = None
        self.split_table()
        self.model = BayesianModel(self.model_table)
        self.row_dict = {}
        self.build_row_dict()

    def split_table(self, ratio=0.7, random_state=None):
        """
        Split the original table into train (model_table) and test (test_table) sets
        """
        self.model_table = self.table.sample(frac=ratio, random_state=random_state).reset_index(drop=True)
        self.test_table = self.table.drop(self.model_table.index).reset_index(drop=True)

    def build_row_dict(self):
        """
        Create a dictionary from the test_table rows without the target column
        """
        for i in range(len(self.test_table)):
            # Extract features only (all columns except the last one)
            self.row_dict[i] = self.test_table.iloc[i, :-1].to_dict()

    def test(self):
        """
        Test the model on the test_table and return accuracy results
        """
        correct = 0
        total = len(self.test_table)
        target_vals = self.test_table.iloc[:, -1]  # target column from test_table

        for i in range(total):
            row = self.row_dict[i]
            predicted = BayesianClassifier.prediction(row, self.model.model, self.model.ratio_target_variable)
            if predicted == target_vals[i]:
                correct += 1

        incorrect = total - correct

        return {
            "correct_count": correct,
            "incorrect_count": incorrect,
            "total": total,
            "success": f"{int(correct * 100 / total)}%"
        }

