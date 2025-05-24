
from fastapi import APIRouter,HTTPException
from starlette import status
from app.api.dependency import db_dependency
from app.schemas.userschema import UserSchema
from app.models.user import User



router=APIRouter()

@router.post("/create-user", status_code=status.HTTP_201_CREATED)
async def create_new_user(
    userdata: UserSchema, db: db_dependency
):
    existing_user = db.query(User).filter(User.email == userdata.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    new_user = User(**userdata.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }