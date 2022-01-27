import pandas as pd
class Document:
    def __init__ (self, docName: str):
        self.docName = docName
        self.xls = pd.ExcelFile(docName)
        self.sheetNames = self.xls.sheet_names
        self.sheets = {}
        for sheet_name in self.sheetNames:
            self.sheets[sheet_name] = self.xls.parse(sheet_name)
