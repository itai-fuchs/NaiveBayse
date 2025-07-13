import pandas as pd


class Cleaner:
    """
    clean data from table
    """

    def __init__(self, csv_file):

        self.table = pd.read_csv(csv_file)
        self.table = self.table.dropna()
        self.drop_index()
        # Remove duplicate rows and reset index (drop old index to avoid extra column)
        self.table = self.table.drop_duplicates().reset_index(drop=True)


    def drop_index(self):
        """
        clean the index columns from table
        :return:
        """
        cols_to_drop = [col for col in self.table.columns if self.table[col].nunique() == self.table.shape[0]]
        self.table = self.table.drop(columns=cols_to_drop)


    # def drop_duplicate_columns(self):
    #
    #
    #
    #     # duplicated = self.table.T.duplicated()
    #     # self.table = self.table.loc[:, ~duplicated]


