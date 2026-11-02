from pydantic import BaseModel, ConfigDict



class ProductSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str
    description: str
    price: int
    image: str
    category: str
    