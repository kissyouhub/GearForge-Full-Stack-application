from fastapi import FastAPI, HTTPException,status, Depends
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.schemas import OrderCreateSchema, OrderRead, OrderReadSchema, ProductCreate, ProductRead  
from app.models import Base, Product
from app.database import engine,get_db, Session
from sqlalchemy import select
from fastapi import FastAPI
from app.service import OrderService

@asynccontextmanager
async def lifespan(_: FastAPI):
    from app.models import Product
    Base.metadata.create_all(bind=engine)
    yield
    
app = FastAPI()



@app.get("/orders/{order_id}", response_model= OrderReadSchema)
def get_order(order_id, order_service: OrderService = Depends(get_order_service)):
    return order_service.get(order_id)

@app.post("/orders/", response_model= OrderReadSchema)
def create_order(payload: OrderCreateSchema, order_service: OrderService = Depends(get_order_service)):
    return order_service.create(payload)

    