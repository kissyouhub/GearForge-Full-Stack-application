from fastapi import FastAPI, HTTPException,status, Depends
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.schemas import PaymentReadSchema, PaymentCreateSchema
from app.models import Base, Product
from app.database import engine,get_db, Session
from sqlalchemy import select
from fastapi import FastAPI
from app.service import PaymentService

@asynccontextmanager
async def lifespan(_: FastAPI):
    from app.models import PaymentORM
    Base.metadata.create_all(bind=engine)
    yield
    
app = FastAPI()



@app.get("payments/{payment_id}", response_model= PaymentReadSchema)
async def get_payment(payment_id, payment_service: PaymentService = Depends(get_payment_service)):
    return await payment_service.get(payment_id)

@app.post("/payments/", response_model= PaymentReadSchema)
async def create_payment(payload: PaymentCreateSchema, payment_service: PaymentService = Depends(get_payment_service)):
    payment = await payment_service.create(payload)
    
    return payment

    