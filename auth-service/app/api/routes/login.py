from fastapi import APIRouter
from starlette import status
from app.schemas.auth import LoginRequest,CreateaccessTokenRequest
from app.api.dependency import db_dependency
from app.models.user import User
from app.core.security import verify_the_password
from fastapi import HTTPException,Response
from app.services.auth import create_access_token,create_refresh_token


router=APIRouter()


@router.post("/login",status_code=status.HTTP_201_CREATED)
async def register_user(userdata:LoginRequest,db:db_dependency,response:Response):
    existing_user=db.query(User).filter(User.email==userdata.email).first()
    if not existing_user:
        raise HTTPException(status_code=404,detail="User not found please register first")
    userpassword=existing_user.password
    isMatching = verify_the_password(userdata.password, userpassword)

    if not isMatching:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    
    token_data=CreateaccessTokenRequest(
        id=existing_user.id,
        name=existing_user.name,
        email=existing_user.email
    )
    access_token=create_access_token(token_data)
    refresh_token=create_refresh_token(token_data)

    response.set_cookie(
        key="refresh_token",
        value=refresh_token["refresh_token"],
        httponly=True,
        secure=True,         
        samesite="none",      
        max_age=60 * 60 * 24 * 7, 
        path="/"
    )

    return {
    "access_token": access_token["access_token"],
    "token_type": "bearer"
}

    
   