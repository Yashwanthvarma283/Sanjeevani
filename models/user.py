from sqlalchemy import Column,Integer,String
from database.db import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,index=True,primary_key=True)
    name=Column(String)