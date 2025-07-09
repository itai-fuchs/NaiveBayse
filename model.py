class Model:
    def __init__(self, clean_table,target_column=None):
        self.table=clean_table
        self.target_column = target_column or self.table.columns[-1]
        self.model = {}
        self.columns= [col for col in self.table if col != self.target_column]

    def create_dict(self):
        for unique_target in self.table[self.target_column].unique():
            self.model[unique_target] = {}
            for col in self.columns:
                self.model[unique_target][col] = {}
                for uniq_value in self.table[col].unique():
                    self.model[unique_target][col][uniq_value]=0
        print(self.model)



    def create_statistical_values(self):

        for key in self.model:
            filtered_table = self.table[self.table[self.target_column] == key]
            for col in self.columns:
                value_count = filtered_table[col].value_counts(normalize=True)
                for val, ratio in value_count.items():
                    self.model[key][col][val] =round(ratio,3)

    def target_variable(self):
         return self.table[self.target_column].value_counts(normalize=True).to_dict()

    def execute(self):
        self.create_dict()
        self.create_statistical_values()








