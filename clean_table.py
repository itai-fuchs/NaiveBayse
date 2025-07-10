import pandas as pd


class Cleaner:
    """
    clean data from table
    """

    def __init__(self, csv_file):

        self.table = pd.read_csv(csv_file)

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

    def execute(self):
        """
        execute all method in class
        :return:
        """
        self.drop_id()
        self.drop_null()
        self.drop_duplicate_columns()
