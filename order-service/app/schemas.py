from gc import set_debug
from unittest.mock import Base

from pydantic import BaseModel, ConfigDict



class OrderCreateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_id: str
    items: list[OrderItemSchema]

class OrderItemSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: str
    quantity: int
    

class OrderItemReadSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    order_id: str
    product_id: str
    product_name: str
    quantity: int
    unit_price: int
    
class OrderReadSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str 
    user_id: str
    status: str 
    total_amount: int
    items: list[OrderItemReadSchema]
    
    