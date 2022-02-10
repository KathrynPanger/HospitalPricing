import pandas as pd

class Document():
    def __init__ (self, data):
        self.data = data
        self.sheetNames = data.sheet_names
        self.sheets = {}
        for sheet_name in self.sheetNames:
            #self.sheets[sheet_name] = data.parse(sheet_name)
            self.sheets[sheet_name] = Sheet(sheet_name, data)

class Sheet():
    def __init__(self, sheetName, data):
        self.sheetName = sheetName
        self.data = data.parse(sheetName)
