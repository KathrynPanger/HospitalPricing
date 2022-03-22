
class Sheet():
    def __init__(self, sheetName, data):
        self.name = sheetName
        self.data = data.parse(sheetName, header=None)

    def __repr__(self):
        return f"Sheet Object: {self.name}"
