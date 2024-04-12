from pydantic import BaseModel

class Request(BaseModel):
    title:str
    body:str
    

class User(BaseModel):
    username:str
    email:str
    password:str
    
class Login(BaseModel):
    username:str
    password:str

class ShowUser(BaseModel):
    username: str
    email:str
    blogs:list[Request]

class ShowBlog(Request):
    creator:ShowUser