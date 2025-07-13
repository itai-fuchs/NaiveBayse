import pandas as pd


class CleanerAndSplit:
    """
    clean data from table
    """

    def __init__(self, csv_file):

        self.table = pd.read_csv(csv_file)
        self.model_table =None
        self.test_table=None
        self.execute()

    def drop_null(self):
        """
        clean nulls from table
        :return:
        """
        self.table = self.table.dropna()

    def drop_id(self):
        """
        clean the id columns from table
        :return:
        """
        if "id" in self.table.columns:
            self.table.drop("id", axis=1, inplace=True)


    def drop_duplicate_columns(self):
        """
        clean duplicate columns from table
        :return:
        """
        duplicated = self.table.T.duplicated()
        self.table = self.table.loc[:, ~duplicated]

    def split_table(self, ratio=0.7, random_state=None):
        """
        Splits table into model and test tables with reset indexes.
        """
        self.model_table = self.table.sample(frac=ratio, random_state=random_state).reset_index(drop=True)
        self.test_table = self.table.drop(self.model_table.index).reset_index(drop=True)

    def execute(self):
        """
        execute all method in class
        :return:
        """
        self.drop_id()
        self.drop_null()
        self.drop_duplicate_columns()
        self.split_table()
