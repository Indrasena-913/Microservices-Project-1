from pydantic import BaseModel, Field



class RegisterRequest(BaseModel):
    name:str = Field(min_length=3)
    email:str =Field(min_length=10)
    password:str = Field(min_length=4)

class CreateaccessTokenRequest(BaseModel):
    id:int
    name:str
    email:str

class LoginRequest(BaseModel):
    email:str
    password:str