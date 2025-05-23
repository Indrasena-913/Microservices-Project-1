from datetime import UTC, datetime, timedelta, timezone
from jose import jwt
from app.schemas.auth import CreateaccessTokenRequest
from app.core.config import settings

ACCESS_TOKEN_EXPIRES_IN=settings.ACCESS_TOKEN_EXPIRES_IN
JWT_SECRET=settings.JWT_SECRET
ALGORITHM=settings.ALGORITHM
REQUEST_TOKEN_EXPIRES_IN=settings.REQUEST_TOKEN_EXPIRES_IN


def create_access_token(userdata:CreateaccessTokenRequest,expires_delta:int=ACCESS_TOKEN_EXPIRES_IN):
    dataencode=userdata.model_dump().copy()
    expires_in=datetime.now(timezone.utc)+timedelta(minutes=expires_delta)
    dataencode["exp"]=int(expires_in.timestamp())
    access_token=jwt.encode(dataencode,JWT_SECRET,algorithm=ALGORITHM)
    return {"type":"access","access_token":access_token}

def create_refresh_token(userdata:CreateaccessTokenRequest,expires_delta:int=REQUEST_TOKEN_EXPIRES_IN):
    dataencode=userdata.model_dump().copy()
    expires_in=datetime.now(timezone.utc)+timedelta(days=expires_delta)
    dataencode["exp"]=int(expires_in.timestamp())
    refresh_token=jwt.encode(dataencode,JWT_SECRET,algorithm=ALGORITHM)
    return {"type":"refresh","refresh_token":refresh_token}
