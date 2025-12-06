from fastapi import status,HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from sqlalchemy.exc import SQLAlchemyError,IntegrityError



def get_user(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} not found') 
        
    return user

def create_user(request:schemas.User,db:Session):
    try:
        new_user = models.User(
            name=request.name,
            email=request.email,
            password=Hash.encrypt(request.password)
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    except IntegrityError as e:
        db.rollback()
        # Example: email already exists (unique constraint)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    except SQLAlchemyError as e:
        db.rollback()
        # General SQL error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

    except Exception as e:
        db.rollback()
        # Any other unexpected error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}"
        )

def destroy(id:int,db:Session):
     db.query(models.User).filter(models.User.id== id).delete(synchronize_session=False)
     db.commit()
   
     return 'done'