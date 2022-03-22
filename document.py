import pandas as pd
from sheet import Sheet

class Document():
    def __init__ (self, name, data):
        self.name = name
        self.data = data
        self.sheetNames = data.sheet_names
        self.sheets = {}
        for sheet_name in self.sheetNames:
            self.sheets[sheet_name] = Sheet(sheet_name, data)
    def __repr__ (self):
        return f"Document Object: {self.name}"

