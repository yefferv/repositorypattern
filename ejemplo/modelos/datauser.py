from ejemplo.infraestructura.datastore import DataStore
from ejemplo.modelos.connection import  StoreException
from ejemplo.dominio.ichildstore import IChildStore
from .usermodel import UserModel
import pandas as pd 


class DataUser(DataStore,IChildStore):
    def add_one(self, user):
        try:
            new_user = [{'id':1 ,'name': user.name}]
            print(new_user)
            new_user = pd.DataFrame(new_user)
            self.add(new_user)            
        except Exception as e:
            print(e)
            raise StoreException('error storing user')

    def get_all(self):
        try:
            users = self.query_all(pd)
            print(users)
            for _,row in users.iterrows():
                print(row['name'])
        except Exception as e:
            print(e)
            raise StoreException('error storing user')



