


class BayesianModel:
    """
    Receives a table (pandas DataFrame) and creates a Naive Bayesian model from the data.
    """

    def __init__(self, table, target_column=None):
        self.table = table
        self.target_column = target_column or self.table.columns[-1]
        self.model = {}
        self.columns = [col for col in self.table if col != self.target_column]
        self.ratio_target_variable = self.table[self.target_column].value_counts(normalize=True).to_dict()
        self.execute()

    def create_dict(self):
        """
        Initializes the structure of the model dictionary with zeros.
        """
        for target_val in self.table[self.target_column].unique():
            self.model[target_val] = {}
            for col in self.columns:
                self.model[target_val][col] = {}
                for val in self.table[col].unique():
                    self.model[target_val][col][val] = 0

    def fill_statistical_values(self):
        """
        Fills the model dictionary with conditional probabilities using Laplace smoothing.
        """
        for target_val in self.model:
            filtered_table = self.table[self.table[self.target_column] == target_val]
            for col in self.columns:
                col_value_counts = filtered_table[col].value_counts()
                total_rows =filtered_table.shape[0]
                col_unique_vals = self.table[col].nunique()

                for val in self.table[col].unique():
                    count = col_value_counts.get(val, 0)
                    smoothed_prob = (count + 1) / (total_rows + col_unique_vals)
                    self.model[target_val][col][val] = round(smoothed_prob, 4)

    def execute(self):
        """
        Executes all steps to build the model.
        """
        self.create_dict()
        self.fill_statistical_values()
