from os import listdir
from os.path import isfile, join
from document import Document
import pandas as pd
from xlrd import XLRDError


class Hospital:
    def __init__(self, path: str):
        self.path = path
        # Hospital name
        self.name = path.split("\\")[-1]
        # Dictionary of files and document objects
        self.documents = {}
        # File
        self.docNames = [f for f in listdir(path) if isfile(join(path, f))]
        for document in self.docNames:
            filename = document.split(".")
            extension = filename[-1]
            correctFileExtensions = ["xls", "xlsx"]
            if extension in correctFileExtensions:
                try:
                    data = pd.ExcelFile(join(path, document))
                    self.documents[document] = Document(data)
                except XLRDError:
                    print(f"XLRDError: document not imported \n "
                          f"{self.name}: {document}")
                    continue
                except IOError:
                    print(f"IOError: document not imported \n "
                          f"{self.name}: {document}")
                except ValueError:
                    continue


            