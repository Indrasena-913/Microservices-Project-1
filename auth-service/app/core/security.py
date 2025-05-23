from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")



def hash_the_password(password:str):
    return pwd_context.hash(password)

def verify_the_password(oldpassword:str,password:str):
    return pwd_context.verify(oldpassword,password)