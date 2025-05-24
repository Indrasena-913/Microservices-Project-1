from fastapi import FastAPI
from app.core.database import engine,Base
from app.models import user
from app.api.routes.createuser import router as createuser_router

app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(createuser_router)


@app.get("/")
async def healthy_check():
    return {"message": "user service is running"}