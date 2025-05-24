from fastapi import APIRouter,HTTPException
from starlette import status
from app.api.dependency import db_dependency
from app.models.user import User
from app.core.security import user_dependency,admin_dependency



router=APIRouter()


@router.get("/users",status_code=status.HTTP_200_OK)
async def register_user(db:db_dependency,admin:admin_dependency):
    if admin.role != "admin":
        raise HTTPException(status_code=401,detail="unauthorized access")
    
    all_users=db.query(User).all()
    if not all_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No users found")
    return all_users
   
   




