

from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, Session
from uuid import uuid4


class Base(DeclarativeBase):
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))
    
    
class Product(Base):
    __tablename__ = "Products"
    
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    image: Mapped[str]
    category: Mapped[str]