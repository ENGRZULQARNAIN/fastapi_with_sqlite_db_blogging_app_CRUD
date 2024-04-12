from database import Base 
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__="blogs"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    user_id=Column(Integer,ForeignKey("user_information.userid"))
    creator=relationship("User_info",back_populates="blogs")

class User_info(Base):
    __tablename__="user_information"
    userid = Column(Integer, primary_key=True,index=True)
    username = Column(String,unique=True)
    email = Column(String, unique=True) 
    password=Column(String)

    blogs=relationship("Blog",back_populates="creator")