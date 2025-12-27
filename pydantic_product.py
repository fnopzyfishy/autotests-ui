from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Цена должна быть больше 0")
    tags: list[str] = []

product_data = {
    "name": "Phone",
    "price": 499.99,
    "tags": ["electronics", "smartphone"]
}

product = Product(**product_data)
print(product)


# Так же можно работать с вложенными моделями

class Market(BaseModel):
    id: int
    name: str

class OnMarket(BaseModel):
    id: int
    name: str
    market: Market

model_market = {
    "id": 1,
    "name":"username",
    "market": {
        "id": 1,
        "name": "username"
    }
}

on_market_obj = OnMarket(**model_market)
print(on_market_obj)