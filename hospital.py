from os import listdir
from os.path import isfile, join
from document import Document
import pandas as pd


class Hospital:
    def __init__(self, path: str):
        self.path = path
        # Hospital name
        self.hospital = path.split("\\")[-1]
        # Dictionary of files and document objects
        self.documents = {}
        # File
        self.docNames = [f for f in listdir(path) if isfile(join(path, f))]
        for document in self.docNames:
            try:
                data = pd.ExcelFile(join(path, document))
                self.documents[document] = Document(data)
            except ValueError:
                continue
            