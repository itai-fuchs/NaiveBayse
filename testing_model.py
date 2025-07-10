from classifier import BayesianClassifier
from clean_table import Cleaner
from bayesian_model import BayesianModel

class TestingModel:
    """
    Performs tests on the model
    """
    def __init__(self,table):
        self.table=table
        self.target_column=self.table.iloc[:,-1]
        self.row_dict={}
        self.model=BayesianModel( self.table)

    def rows_dict(self):
        """
        Creates a dictionary of the rows in the table
        :return:
        """
        for index, row in self.table.iterrows():
            row_without_target = row.drop(labels=self.table.columns[-1])
            self.row_dict[index] = row_without_target.to_dict()

    def test(self):
        """
        Performs a test on the accuracy of the model
        :return:
        """
        correct = 0
        total = self.table.shape[0]

        for i in range(total):
            row = self.row_dict[i]

            predicted = BayesianClassifier.prediction(row, self.model, self.target_column)

            if predicted == self.target_column.iloc[i]:
                correct += 1

        incorrect = total - correct

        return {
            "correct_ratio": correct / total,
            "incorrect_ratio": incorrect / total,
            "correct_count": correct,
            "incorrect_count": incorrect,
            "total": total
        }




ct = Cleaner("C:/Users/itai/Downloads/buy_computer_data.csv")
ct.execute()

tm=TestingModel(ct.table)
tm.rows_dict()
print(tm.row_dict)


