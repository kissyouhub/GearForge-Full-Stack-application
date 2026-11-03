from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, Session
from app.config import settings






engine = create_engine(settings.database_url, echo=True)

Sessionlocal = sessionmaker[Session](bind=engine)

def get_db():
    db = Sessionlocal()
    
    try:
        yield db
    finally:
        db.close()