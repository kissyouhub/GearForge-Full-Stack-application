

import httpx

class CatalogClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        
    def get_product(self, product_id: str) -> dict:
        response = httpx.get(f"{self.base_url}/{product_id}")
        return response.json()
    
if __name__ == "__main__":
    client = CatalogClient(base_url="http://localhost:8000")
    product = client.get_product(product_id="207180d9-7597-44ef-be35-1dad566eb7b3")
    print(product)