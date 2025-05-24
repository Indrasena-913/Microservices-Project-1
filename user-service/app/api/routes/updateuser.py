from fastapi import APIRouter,HTTPException, Path
from starlette import status
from app.api.dependency import db_dependency
from app.models.user import User
from app.core.security import user_dependency
from app.schemas.userschema import UpdateUser



router=APIRouter()


@router.put("/users/{user_id}",status_code=status.HTTP_201_CREATED)
async def update_the_user(db:db_dependency,user:user_dependency,updated_data:UpdateUser,user_id:int=Path(gt=0)): 
    print(user)
    if not user:
        raise HTTPException(status_code=401,detail="unauthorized access")
    
    existing_user=db.query(User).filter(User.id==user_id).first()
    if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No user found")
    if updated_data.name is not None:
        existing_user.name = updated_data.name

    if updated_data.email is not None:
        existing_user.email = updated_data.email
    db.add(existing_user)
    db.commit()
    db.refresh(existing_user)

    
   
    return existing_user
   
   




