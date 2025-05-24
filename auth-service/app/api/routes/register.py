from fastapi import APIRouter,HTTPException
from starlette import status
from app.schemas.auth import RegisterRequest
from app.api.dependency import db_dependency
from app.models.user import User
from app.core.security import hash_the_password
import httpx
from app.core.config import settings

USER_SERVICE_URL=settings.USER_SERVICE_CREATE_USER_URL


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

    user_service_payload = {
        "name": userdata.name,
        "email": userdata.email,
        "password":hashedpassword,
        "role": "admin"  
    }

    async with httpx.AsyncClient() as client:
        try:
            response=await client.post(USER_SERVICE_URL,json=user_service_payload)
            response.raise_for_status()
        except Exception as e:
            print(f"User Service API call failed: {e}")
            db.delete(new_user)
            db.commit()

            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="user data is not added into user service")
    return {
        "message":"user registered successfully",
        "id":new_user.id,
         "user_service_response": response.json()
    }


    


