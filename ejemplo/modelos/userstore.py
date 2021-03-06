from ejemplo.infraestructura.store import Store
from ejemplo.modelos.connection import  StoreException
from ejemplo.dominio.ichildstore import IChildStore
from .usermodel import UserModel


class UserStore(Store,IChildStore):
    def add_one(self, user):
        try:
            new_user = UserModel(name=user.name)
            self.add(new_user)            
        except Exception as e:
            print(e)
            raise StoreException('error storing user')

    def get_all(self):
        try:
            users = self.query_all(UserModel)
            for row in users:
                print(row)
        except Exception as e:
            print(e)
            raise StoreException('error storing user')



