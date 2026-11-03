

from datetime import datetime

from time import timezone

from click import DateTime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, Session, relationship
from uuid import uuid4


class Base(DeclarativeBase):
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    
    

class PaymentORM(Base):
    __tablename__ = "payments"
 
    order_id: Mapped[str]
    status: Mapped[str]
    amount: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        server_default=func.now(),
        nullable=False,
    )