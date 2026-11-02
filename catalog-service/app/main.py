from fastapi import FastAPI,status, Depends
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings

from app.models import Base
from app.database import engine

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_: FastAPI):
    from app.models import Product
    Base.metadata.create_all(bind=engine)
    yield
    
settings = get_settings()
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

