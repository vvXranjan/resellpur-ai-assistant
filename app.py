from fastapi import FastAPI
from pydantic import BaseModel
import agents

app = FastAPI()

# Input models
class Product(BaseModel):
    id: int
    title: str
    category: str
    brand: str
    condition: str
    age_months: int
    asking_price: float
    location: str

class Message(BaseModel):
    id: int
    content: str

# Endpoints
@app.post("/negotiate")
def negotiate(product: Product):
    return agents.price_suggestor(product.dict())

@app.post("/moderate")
def moderate(message: Message):
    return agents.chat_moderator(message.content, message.id)
