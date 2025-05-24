from fastapi import Request, Response, HTTPException
from starlette import status
from jose import jwt, JWTError
from app.core.config import settings
from app.api.dependency import db_dependency
from app.models.user import User
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

JWT_SECRET = settings.JWT_SECRET
ALGORITHM = settings.ALGORITHM


def get_the_current_user(req: Request, res: Response, db: db_dependency):
    token = req.headers.get("Authorization")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization token is missing"
        )
    
    try:
        bearer, token = token.split(" ")
        if bearer.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Authorization type must be Bearer"
            )

        user_data = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        print(user_data)

        if not user_data :
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        existing_user = db.query(User).filter(User.email == user_data["email"]).first()

        if not existing_user:
            raise HTTPException(status_code=404, detail="User does not exist")
        if existing_user.role != "admin":
            raise HTTPException(status_code=401, detail="Unauthorized access")

        return existing_user  

    except JWTError:
        raise HTTPException(status_code=401, detail="Token is invalid or expired")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid token format")


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise Exception("Invalid or expired refresh token")



admin_dependency=Annotated[Session,Depends(get_the_current_user)]
user_dependency=Annotated[Session,Depends(verify_access_token)]