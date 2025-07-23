import pandas as pd
import logging


class Cleaner:
    """
    clean data from table
    """

    def __init__(self, table):
        logging.info(f"Initializing Cleaner with table of shape {table.shape}")
        self.table = table
        self.table = self.table.dropna()
        logging.info(f"Table shape after dropna: {self.table.shape}")
        self.drop_index()
        # Remove duplicate rows and reset index.
        self.table = self.table.drop_duplicates().reset_index(drop=True)
        logging.info(f"Table shape after dropping duplicates and resetting index: {self.table.shape}")

    def drop_index(self):
        """
        clean the index columns from table
        :return:
        """
        cols_to_drop = [col for col in self.table.columns if self.table[col].nunique() == self.table.shape[0]]
        if cols_to_drop:
            logging.info(f"Dropping index-like columns: {cols_to_drop}")
        else:
            logging.info("No index-like columns to drop")
        self.table = self.table.drop(columns=cols_to_drop)
