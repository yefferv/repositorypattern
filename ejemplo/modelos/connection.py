from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///testRepo.sqlite')


def get_connection():
       return engine

class StoreException(Exception):
       def __init__(self, message, *errors):
           Exception.__init__(self, message)
           self.errors = errors