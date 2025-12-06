
from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..controller import user_controller

router =APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session= Depends(get_db)):
  return user_controller.get_user(id,db)

@router.post('',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session= Depends(get_db)):
   return user_controller.create_user(request,db)
    

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db)):
   return user_controller.destroy(id,db)