from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
load_dotenv()




class Settings(BaseSettings):
    DATABASE_URL:str
    ACCESS_TOKEN_EXPIRES_IN:int
    JWT_SECRET:str
    ALGORITHM:str
    REQUEST_TOKEN_EXPIRES_IN:int


    class Config:
            env_file="../.env"

settings=Settings()