from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")



def hash_the_password(password:str):
    return pwd_context.hash(password)

def verify_the_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
