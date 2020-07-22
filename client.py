from ejemplo.modelos.userstore import  UserStore
from ejemplo.modelos.animalstore import  AnimalStore
from ejemplo.modelos.usermodel import UserModel
from ejemplo.modelos.datauser import DataUser
from ejemplo.dominio.animal import  Animal
from ejemplo.dominio.user import  User
from ejemplo.modelos.connection import  StoreException, Base, engine


Base.metadata.create_all(engine)

try:
    #para manejar base datos sqlite
    #with UserStore() as user_store:

    #para manejar archivos csv 
    with DataUser() as user_store:
        user_store.add_one(User('carolina'))
        user_store.complete()
        user_store.get_all()
        user_store.complete()

    print("successfully...")
except StoreException as e:
       print('pruebas : ',e)