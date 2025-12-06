from sqlalchemy.orm import Session
from fastapi import  status,HTTPException
from .. import models,schemas

def get_all(db:Session):
        blogs=db.query(models.Blog).all()
        return blogs
    
def create_blog(db:Session,request):
    new_blog= models.Blog(title=request.title,body=request.body,user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog    

def get_by_id(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # response.status_code= status.HTTP_404_NOT_FOUND
        # return {'detail':f"Blog with id {id} is not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not available")
    return blog

def delete_blog(id:int,db:Session):
    db.query(models.Blog).filter(models.Blog.id== id).delete(synchronize_session=False)
    db.commit()
   
    return 'done' 

def update_blog(id:int,request:schemas.Blog,db:Session):
    
    blog=db.query(models.Blog).filter(models.Blog.id== id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
    blog.update({
        "title":request.title,
        "body":request.body,
        "user_id":request.user_id
     })
    db.commit()
    return {'updated'}   