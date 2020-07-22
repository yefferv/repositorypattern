import os
import pandas as pd
from ejemplo.dominio.istore import IStore


class DataStore(IStore):
    
    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        print(self.ROOT_DIR)
        self.filename = "data.csv"
        self.FILE_PATH = os.path.join(self.ROOT_DIR,  self.filename)
        print(self.FILE_PATH)


    def query_all(self,obj):
        df = obj.read_csv(filepath_or_buffer = self.FILE_PATH, sep=",")
        return df

    def add(self,obj):
        obj.to_csv(self.filename)

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        pass

    def complete(self):
        pass


