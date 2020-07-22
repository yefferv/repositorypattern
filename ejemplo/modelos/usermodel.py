from sqlalchemy import Column, Integer,String
from .connection import Base

class UserModel(Base):
    __tablename__="User"
    id= Column(Integer,primary_key = True)
    name= Column(String,nullable = True)

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'