from fastapi import FastAPI,status,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from database import engine
from models import Base
from schema import Request,ShowBlog
from fastapi import Depends
from models import Blog
import blogs,users
from database import get_db
Base.metadata.create_all(engine)


app=FastAPI(title="Blogging App",version=1.0,)

app.include_router(users.router)
app.include_router(blogs.router)


######################################################################################
