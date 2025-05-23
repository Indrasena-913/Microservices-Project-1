from fastapi import APIRouter
from starlette import status
from app.schemas.auth import RegisterRequest
from app.api.dependency import db_dependency
from app.models.user import User
from app.core.security import hash_the_password


router=APIRouter()


@router.post("/register",status_code=status.HTTP_201_CREATED)
async def register_user(userdata:RegisterRequest,db:db_dependency):
    hashedpassword=hash_the_password(userdata.password)
    new_user=User(
        name=userdata.name,
        password=hashedpassword,
        email=userdata.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"success":"New user created successfully","id":new_user.id,"name":new_user.name}
