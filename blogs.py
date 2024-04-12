from fastapi import APIRouter,Depends,status,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from schema import Request,ShowBlog
from models import Blog



router=APIRouter(tags=["Blogs"])

@router.post("/create_blogs",status_code=status.HTTP_201_CREATED)
async def data(request:Request,db:Session=Depends(get_db)):
    """Insert new data into the database"""
    new_blog=Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
####################################################################################



@router.get("/blogs/{id}",status_code=status.HTTP_302_FOUND,response_model=ShowBlog)
async def read_blog(id:int,db:Session=Depends(get_db)):
    blog=db.query(Blog).filter(Blog.id==id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No blog with this id")
    else:  
        return blog 
#####################################################################################    

    
@router.put("/update_blog/{id}",status_code=status.HTTP_202_ACCEPTED)
async def update_blog(id:int,request:Request,db:Session=Depends(get_db)):
    blog=db.query(Blog).filter(Blog.id==id).first()
    if blog is None:
        message=f"No blog found with id:{id}"
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=message)
    else:            
        blog.title=request.title or blog.title
        blog.body=request.body or blog.body
        db.commit()     
        return {"blog":"blog with id {id} has been updated"}
#########################################################################################

        
@router.delete("/delete_blog/{id}")
async def delete_blog(id:int,db:Session=Depends(get_db)):
    blog=db.query(Blog).filter(Blog.id==id).first()
    if blog is None:
        message=f"Blog with id:{id} was already deleted"
        raise HTTPException(status_code=404,detail=message)
    else:
        db.delete(blog)
        db.commit()
        return {"message":f"Blog of id:{id} has been deleted"}      
#########################################################################################
