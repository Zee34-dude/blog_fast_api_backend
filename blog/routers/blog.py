from fastapi import  APIRouter,Depends,status,Response,HTTPException
from .. import schemas, oaut2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..controller import blog_controller




router =APIRouter(
    prefix='/blog',
    tags=['blogs'],
   dependencies=[Depends(oaut2.get_current_user)]  
)



@router.get('',status_code=status.HTTP_201_CREATED,response_model=List[schemas.ShowBlog])
def all(db:Session= Depends(get_db)):
    return blog_controller.get_all(db)


@router.post('',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,db:Session= Depends(get_db)):
   return blog_controller.create_blog(db,request)

@router.get('/{id}',status_code=200, response_model=schemas.ShowBlog)
def select(id:int,db:Session= Depends(get_db)):
   return blog_controller.get_by_id(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
   return blog_controller.delete_blog(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session= Depends(get_db)):
  return blog_controller.update_blog(id,request,db)


