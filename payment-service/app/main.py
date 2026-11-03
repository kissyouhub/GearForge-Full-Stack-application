from fastapi import FastAPI, HTTPException, Request,status, Depends
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.schemas import PaymentReadSchema, PaymentCreateSchema
from app.models import Base, Product
from app.database import engine,get_db, Session
from sqlalchemy import select
from fastapi import FastAPI
from app.service import PaymentService
from rabbitmq import declare_payment_exchange, connect_rabbitmq
@asynccontextmanager
async def lifespan(app: FastAPI):
    from app.models import PaymentORM
    Base.metadata.create_all(bind=engine)
    connection = await connect_rabbitmq(url=settings.rabbitmq_url)
    channel = await connection.channel()
    app.state.payment_exchange = await declare_payment_exchange(channel, settings.payment_exchange_name)
    
    yield
    
app = FastAPI()



@app.get("payments/{payment_id}", response_model= PaymentReadSchema)
async def get_payment(payment_id, payment_service: PaymentService = Depends(get_payment_service)):
    return await payment_service.get(payment_id)

@app.post("/payments/", response_model= PaymentReadSchema)
async def create_payment(request: Request, payload: PaymentCreateSchema, payment_service: PaymentService = Depends(get_payment_service)):
    payment = await payment_service.create(payload)
    
    await payment_service.complete_payment(payment, order_id=payload.order_id, user_id=payload.user_id, amount= payload.amount, exchange=request.app.state.payment_exchange)

    