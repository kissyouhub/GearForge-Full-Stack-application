from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, Session
from app.config import get_settings



settings = get_settings()


engine = create_engine(settings.DATABASE_URL, echo=True)

Sessionlocal = sessionmaker[Session](bind=engine)

def get_db():
    db = Sessionlocal()
    
    try:
        yield db
    finally:
        db.close()