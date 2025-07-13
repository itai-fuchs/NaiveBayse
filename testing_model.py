from classifier import BayesianClassifier
from Clean_And_Split_Table import CleanerAndSplit
from bayesian_model import BayesianModel

class TestingModel:
    """
    Performs tests on the model
    """
    def __init__(self,table):
        self.table=table
        self.target_column=self.table.iloc[:,-1]
        self.row_dict={}
        self.model=BayesianModel(self.table)
        self.rows_dict()


    def rows_dict(self):
        """
        Creates a dictionary of the rows in the table
        :return:
        """
        self.table = self.table.iloc[:, :-1]
        for i in range(len(self.table)):
            self.row_dict[i] = self.table.iloc[i].to_dict()

    def test(self):
        """
        Performs a test on the accuracy of the model
        :return:
        """
        correct = 0
        incorrect=0
        total = self.table.shape[0]

        for i in range(total):

            row = self.row_dict[i]

            predicted = BayesianClassifier.prediction(row, self.model.model,self.model.ratio_target_variable)

            if predicted == self.target_column[i]:
             correct+=1
        incorrect = total - correct


        return {
            "correct_count": correct,
            "incorrect_count": incorrect,
            "total": total,
            "succses":f"{int(correct*100/total)}%"
        }

