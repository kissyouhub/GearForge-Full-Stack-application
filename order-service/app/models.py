

from datetime import datetime

from time import timezone

from click import DateTime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, Session, relationship
from uuid import uuid4


class Base(DeclarativeBase):
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    
    
class Order(Base):
    __tablename__ = "orders"
    
    user_id: Mapped[int]
    status: Mapped[str]
    total_amount: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        server_default=func.now(),
        nullable=False,
    )
    items: Mapped[list[OrderItem]] = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"
 
    order_id = Mapped[str] = mapped_column(ForeignKey("orders.id"))
    product_id = Mapped[str]
    product_name = Mapped(str)
    quantity = Mapped[int]
    unit_price = Mapped[int]
    order: Mapped[Order] = relationship("Order", back_populates="items")