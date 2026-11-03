
from urllib import response
from xml.dom import NotFoundErr

from sqlalchemy.orm import Session
from app.models import Order
from app.config import NotFoundError
from schemas import OrderCreateSchema
from catalog_client import CatalogClient
class OrderService():
    def __init__(self, session: Session, catalog_client: CatalogClient):
        self.session = session
        self.catalog_client = catalog_client
        
    def get(self, order_id: str):
        order = self.session.get(Order, order_id)
        if order is None:
            raise NotFoundError
        return order
    
    def create(self, order_data: OrderCreateSchema):
        products = []
        for item in order_data.items:
            product = self.catalog_client.get_product(product.product_id)