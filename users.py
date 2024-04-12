from fastapi import APIRouter,Depends,status,HTTPException

from schema import User,Login,ShowUser
from sqlalchemy.orm import Session
from database import get_db


from hashing import Hasher

from models import User_info

router=APIRouter(tags=["Users"])





@router.post("/create_account")
def create_user(request:User,db:Session=Depends(get_db)):
    hashed=Hasher.get_password_hash(request.password)
    new_user=User_info(username=request.username,email=request.email,password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"Account created successfully!"}  


@router.post("/login",status_code=status.HTTP_200_OK)
def login_user(request:Login,db:Session=Depends(get_db)):
    user=db.query(User_info).filter(User_info.username == request.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username!")
    elif not Hasher.verify_password(request.password,user.password):
        raise HTTPException(status_code=    401, detail="Wrong password!")
    else:
        return {"message":"lOGGED IN SUCCESFULLY"}
    


@router.get("/user{id}",status_code=status.HTTP_202_ACCEPTED,response_model=ShowUser)
def get_one_user(id:int,db: Session = Depends(get_db)):
    user=db.query(User_info).filter(User_info.userid==id).first()
    if user is None:
        raise HTTPException(status_code=404,detail=f"No User found with id:{id}")
    return user
