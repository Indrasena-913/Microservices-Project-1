from datetime import datetime,timezone
from sqlalchemy import Column, DateTime,Integer,String
from app.core.database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    created_at=Column(DateTime(timezone=True),default=lambda:datetime.now(timezone.utc))