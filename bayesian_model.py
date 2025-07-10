

class BayesianModel:

    """
Receives a table and creates a Bayesian model on the information
    """
    def __init__(self, table,target_column=None):
        self.table=table
        self.target_column = target_column or self.table.columns[-1]
        self.model = {}

        self.columns= [col for col in self.table if col != self.target_column]

        self.ratio_target_variable=self.table[self.target_column].value_counts(normalize=True).to_dict()

    def create_dict(self):
        """
        create model dict shape fills with zeros
        :return:
        """
        for unique_target in self.table[self.target_column].unique():
            self.model[unique_target] = {}
            for col in self.columns:
                self.model[unique_target][col] = {}
                for uniq_value in self.table[col].unique():
                    self.model[unique_target][col][uniq_value]=0
        print(self.model)

    def  fill_statistical_values(self):
        """
         Fills_in_statistical_values model dict
        :return:
        """
        for key in self.model:
            filtered_table = self.table[self.table[self.target_column] == key]
            for col in self.columns:
                value_count = filtered_table[col].value_counts(normalize=True)
                for val, ratio in value_count.items():
                    self.model[key][col][val] =round(ratio,3)

    def execute(self):
        """
        execute the model creating.
        :return:
        """
        self.create_dict()
        self.fill_statistical_values()
        self.ratio_target_variable()








