from fastapi import APIRouter, Request, HTTPException, status
from app.services.auth import verify_refresh_token, create_access_token

router = APIRouter()

@router.post("/refresh", status_code=status.HTTP_200_OK)
async def refresh_access_token(request: Request):
    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        raise HTTPException(status_code=401, detail="Refresh token missing")

    try:
        token_data = verify_refresh_token(refresh_token)  
    except Exception as e:
        raise HTTPException(status_code=403, detail="Invalid or expired refresh token")

    new_access_token = create_access_token(token_data)

    return {
        "access_token": new_access_token["access_token"],
        "token_type": "bearer"
    }
