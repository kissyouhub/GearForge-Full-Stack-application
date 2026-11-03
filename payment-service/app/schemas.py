from gc import set_debug
from unittest.mock import Base

from pydantic import BaseModel, ConfigDict



class PaymentCreateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    order_id: str
    user_id: int
    amount: int

class PaymentReadSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str 
    order_id: str
    user_id: int
    amount: int
   
    
    