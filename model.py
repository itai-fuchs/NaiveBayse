import pandas as pd
from clean_table import clean_csv


class Model:
    def __init__(self, table,target_column=None):
        self.table=table
        self.target_column = target_column or self.table.columns[-1]
        self.model = {}
        self.features= [col for col in self.table if col != self.target_column]

    def find_unique_target(self):
        for unique_target in self.table[self.target_column].unique():
            self.model[unique_target] = {}

    def feel_keys(self):
        for key in self.model:
            for feature in self.features:
                self.model[key][feature] = {}

    def statistical_values(self):
        for key in self.model:
            filtered_table = self.table[self.table[self.target_column] == key]
            for feature in self.features:
                value_count = filtered_table[feature].value_counts(normalize=True)
                for val, ratio in value_count.items():
                    self.model[key][feature][val] =round(ratio,3)

    def target_variable(self):
        self.model[self.target_column] = self.table[self.target_column].value_counts(normalize=True).to_dict()

    # def statistical_values_demo(self):
    #     columns = [col for col in self.table if col != self.target_column and col != "id"]
    #
    #     uniq_targets=self.table[self.target_column].unique()
    #     for uniq_target in uniq_targets:
    #        self.model[uniq_target]={}
    #        for col in columns:
    #             self.model[uniq_target][col]={}
    #             for uniq_val in self.table[col].unique():
    #                 subset = self.table[self.table[self.target_column] == uniq_target]
    #                 count = (subset[col] == uniq_val).sum()
    #                 total = len(subset)
    #                 prob = count / total if total > 0 else 0.0
    #                 self.model[uniq_target][col][uniq_val] = prob
    #                 # self.model[uniq_target][col][uniq_val]={}



    def manage_zero(self):
        pass



ct=clean_csv("C:/Users/itai/Downloads/buy_computer_data.csv")

ct.drop_Null()
ct.drop_id()
ct.drop_duplicate_columns()

m=Model(ct.table)
m.find_unique_target()
m.feel_keys()
m.statistical_values()
print(m.model)



