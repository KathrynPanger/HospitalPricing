from os import listdir
from os.path import isfile, join

class Hospital:
    def __init__(self, path: str):
        # Hospital name
        self.path = path
        self.hospital = path.split("\\")[-1]
        # Files
        self.docNames = [f for f in listdir(path) if isfile(join(path, f))]



