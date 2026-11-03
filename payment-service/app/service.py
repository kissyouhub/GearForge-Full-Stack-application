
from urllib import response
from xml.dom import NotFoundErr

from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Order, OrderItem, PaymentORM
from app.config import NotFoundError
from schemas import OrderCreateSchema, OrderReadSchema, PaymentCreateSchema, PaymentReadSchema
from catalog_client import CatalogClient


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