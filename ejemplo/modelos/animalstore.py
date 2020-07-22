from ejemplo.infraestructura.store import Store
from ejemplo.modelos.connection import  StoreException


# store for Animal obects
class AnimalStore(Store):
    def add_animal(self, animal):
        try:
            c = self.conn.cursor()
            # this needs an appropriate table
            c.execute('INSERT INTO animal (name) VALUES(?)', (animal.name,))
        except Exception:
            raise StoreException('error storing animal ')