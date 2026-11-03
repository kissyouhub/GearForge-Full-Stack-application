from uuid import uuid4

from aio_pika.abc import AbstractRobustConnection, AbstractChannel, AbstractExchange
from urllib import response
from xml.dom import NotFoundErr
from asyncio import sleep
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Order, OrderItem, PaymentORM
from app.config import NotFoundError, settings
from schemas import OrderCreateSchema, OrderReadSchema, PaymentCreateSchema, PaymentReadSchema
from catalog_client import CatalogClient
from rabbitmq import event_publish_json

class PaymentService():
    
    async def __init__(self, session: AsyncSession):
        self.session = session
       
        
    async def get(self, order_id: str):
        payment = await self.session.get(Order, order_id)
        if payment is None:
            raise NotFoundError
        return payment
    
    async def create(self, payment_data: PaymentCreateSchema) -> PaymentReadSchema:
        payment = PaymentORM(order_id = payment_data.order_id, status = "created", amount = payment_data.amount)
        self.session.add(payment)
        await self.session.commit()
        return PaymentReadSchema.model_validate(payment)
    
    async def complete_payment(self, payment: PaymentORM, exchange: AbstractExchange, order_id: str, user_id: str, amount: int):
        await sleep(4)
        
        
        payment.status = "succeed"
        await self.session.commit()
        
        
        event = {
            "event_id": str(uuid4),
            "order_id": order_id,
            "user_id": user_id,
            "status": "succeeded",
            "amount": amount,
            
        }
        await event_publish_json(exchange, settings.payment_succeeded_routing_key, data = event)