from fastapi import APIRouter,HTTPException, Path
from starlette import status
from app.api.dependency import db_dependency
from app.models.user import User
from app.core.security import user_dependency



router=APIRouter()


@router.get("/users/{user_id}",status_code=status.HTTP_200_OK)
async def get_single_user(db:db_dependency,admin:user_dependency,user_id:int=Path(gt=0)):
    if admin.role != "admin":
        raise HTTPException(status_code=401,detail="unauthorized access")
    
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    return user
   
   




