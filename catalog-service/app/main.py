
from fastapi import FastAPI, HTTPException,status, Depends
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.schemas import ProductCreate, ProductRead
from app.models import Base, Product
from app.database import engine,get_db, Session
from sqlalchemy import select
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_: FastAPI):
    from app.models import Product
    Base.metadata.create_all(bind=engine)
    yield
    

app = FastAPI(lifespan=lifespan)


@app.get("/products", response_model = list[ProductRead])
def get_products(db: Session = Depends(get_db)):
        query = select(Product).order_by(Product.name)
        return db.scalars(query).all()
    
@app.get("/{product_id}", response_model= ProductRead)
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "Товар не найден"
            
        )
    return product

@app.post("/", response_model=ProductCreate)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)) -> ProductCreate:
    product = Product(**payload.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
