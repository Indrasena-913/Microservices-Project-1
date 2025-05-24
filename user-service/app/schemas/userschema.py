from pydantic import BaseModel,Field



class UserSchema(BaseModel):
    name:str = Field(min_length=3)
    email:str =Field(min_length=10)
    password:str = Field(min_length=4)
    # role:str

class UpdateUser(BaseModel):
    name:str = Field(min_length=3)
    email:str =Field(min_length=10)