import pandas as pd
import os

class FileConverter:
    """
    A class to convert various file formats into CSV.
    """

    def __init__(self, file):
        """
        Initialize the FileConverter with a file path.
        """
        if not os.path.exists(file):
            raise FileNotFoundError(f"File not found: {file}")
        self.file = file
        self.extension = os.path.splitext(file)[-1].lower()
        self.table = None

    def convert_to_csv(self, output_file=None):
        """
        Load the file and convert it to CSV format.
        If output_file is not specified, it will use the same name with .csv extension.
        """
        self.table = self.load_file()

        if output_file is None:
            output_file = os.path.splitext(self.file)[0] + ".csv"

        self.table.to_csv(output_file, index=False)
        print(f"File converted and saved as CSV: {output_file}")

    def load_file(self):
        """
        Detect the file type and load it as a pandas DataFrame.
        """
        if self.extension == ".csv":
            return pd.read_csv(self.file)
        elif self.extension == ".json":
            return pd.read_json(self.file)
        elif self.extension in [".xls", ".xlsx"]:
            return pd.read_excel(self.file)
        elif self.extension == ".txt":
            return pd.read_csv(self.file, delimiter="\t")
        elif self.extension == ".html":
            return pd.read_html(self.file)[0]
        else:
            raise ValueError(f"Unsupported file format: {self.extension}")
