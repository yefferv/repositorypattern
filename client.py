from ejemplo.modelos.userstore import  UserStore
from ejemplo.modelos.animalstore import  AnimalStore
from ejemplo.modelos.usermodel import UserModel
from ejemplo.dominio.animal import  Animal
from ejemplo.dominio.user import  User
from ejemplo.modelos.connection import  StoreException, Base, engine


Base.metadata.create_all(engine)

try:
    with UserStore() as user_store:
        user_store.add_user(User('sonia'))
        user_store.complete()
        user_store.get_user()
        user_store.complete()
        print("successfully...")
except StoreException as e:
       print('pruebas : ',e)