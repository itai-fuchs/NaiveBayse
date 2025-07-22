import pandas as pd
import os
import logging


class Loader:
    """
    A class to convert various file formats into CSV.
    """

    def __init__(self, file):
        """
        Initialize the Loader with a file path.
        Loads the file immediately and converts it to CSV.
        """
        logging.info(f"Initializing Loader with file: {file}")
        if not os.path.exists(file):
            logging.error(f"File not found: {file}")
            raise FileNotFoundError(f"File not found: {file}")

        self.file = file
        self.extension = os.path.splitext(file)[-1].lower()
        logging.info(f"Detected file extension: {self.extension}")
        self.table = self.load_file()
        self.convert_to_csv()

    def convert_to_csv(self, output_file=None):
        """
        Convert the loaded file to CSV format.
        If output_file is not specified, it will use the same name with .csv extension.
        """
        if output_file is None:
            output_file = os.path.splitext(self.file)[0] + ".csv"

        self.table.to_csv(output_file, index=False)
        logging.info(f"File converted and saved as CSV: {output_file}")

    def load_file(self):
        """
        Detect the file type and load it as a pandas DataFrame.
        """
        logging.info(f"Loading file: {self.file}")
        if self.extension == ".csv":
            df = pd.read_csv(self.file)
        elif self.extension == ".json":
            df = pd.read_json(self.file)
        elif self.extension in [".xls", ".xlsx"]:
            df = pd.read_excel(self.file)
        elif self.extension == ".txt":
            df = pd.read_csv(self.file, delimiter="\t")
        elif self.extension == ".html":
            df = pd.read_html(self.file)[0]
        else:
            logging.error(f"Unsupported file format: {self.extension}")
            raise ValueError(f"Unsupported file format: {self.extension}")
        logging.info(f"File loaded successfully with shape {df.shape}")
        return df
