
from sqlalchemy.orm import Session
from app.service import OrderService
from app.config import settings
from app.database import get_db
from fastapi import Depends
from app.service import PaymentService

def get_payment_service(
    db: Session = Depends(get_db),
) -> PaymentService:
    return PaymentService(db)

