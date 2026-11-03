from fastapi import FastAPI, HTTPException,status, Depends
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.schemas import OrderRead, OrderReadSchema, ProductCreate, ProductRead  
from app.models import Base, Product
from app.database import engine,get_db, Session
from sqlalchemy import select
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_: FastAPI):
    from app.models import Product
    Base.metadata.create_all(bind=engine)
    yield
    
app = FastAPI()




    
    