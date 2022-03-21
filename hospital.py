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
        self.failedDocs = {"XLRDError":[], "IOError":[], "ValueError":[],
                           "OtherError":[] }
        # File
        self.docNames = [f for f in listdir(path) if isfile(join(path, f))]
        for docName in self.docNames:
            filename = docName.split(".")
            extension = filename[-1]
            correctFileExtensions = ["xls", "xlsx"]
            if extension in correctFileExtensions:
                try:
                    data = pd.ExcelFile(join(path, docName))
                    self.documents[docName] = Document(docName, data)
                except XLRDError:
                    print(f"XLRDError: document not imported \n "
                          f"{self.name}: {docName}")
                    self.failedDocs["XLRDError"].append(docName)
                    continue
                except IOError:
                    print(f"IOError: document not imported \n "
                          f"{self.name}: {docName}")
                    self.failedDocs["IOError"].append(docName)
                except ValueError:
                    self.failedDocs["ValueError"].append(docName)
                    continue
                except:
                    print(f"Unknown Error: document not imported \n "
                          f"{self.name}: {docName}")
                    self.failedDocs["OtherError"].append(docName)
    def __repr__ (self):
        return self.name


            