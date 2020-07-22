from ejemplo.modelos.connection import  StoreException, get_connection
from sqlalchemy.orm import sessionmaker
from ejemplo.dominio.istore import IStore


class Store(IStore):
    def __init__(self):
        try:
            Session = sessionmaker(bind=get_connection())
            self.session = Session()
        except Exception as e:
            raise StoreException(*e.args)
        self._complete = False

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        # can test for type and handle different situations
        self.close()

    def complete(self):
        self._complete = True

    def close(self):
        if self.session:
            try:
                if self._complete:
                    self.session.commit()
                else:
                    self.session.rollback()
            except Exception as e:
                raise StoreException(*e.args)
            finally:
                try:
                    self.session.close()
                except Exception as e:
                    raise StoreException(*e.args)

    def add(self,obj):
        self.session.add(obj)
        self.session.commit()

    def query_all(self,obj):
        return self.session.query(obj).all()
                
        