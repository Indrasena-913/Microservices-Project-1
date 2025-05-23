from fastapi import FastAPI
from app.core.database import Base,engine
from app.models import user
from app.api.routes.register import router as register_router
from app.api.routes.login import router as login_router
from app.api.routes.refresh import router as refresh_router

app = FastAPI()
Base.metadata.create_all(bind=engine)


app.include_router(register_router)
app.include_router(login_router)
app.include_router(refresh_router)

@app.get("/")  
async def root():
    return {"message": "hello"}  