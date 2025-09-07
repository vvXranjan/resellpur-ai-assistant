import requests

# URL of the running FastAPI app
url_price = "http://127.0.0.1:8000/negotiate"
url_chat = "http://127.0.0.1:8000/moderate"

# Example product for price suggestion
product = {
    "id": 1,
    "title": "iPhone 12",
    "category": "Mobile",
    "brand": "Apple",
    "condition": "Good",
    "age_months": 24,
    "asking_price": 35000,
    "location": "Mumbai"
}

# Example message for chat moderation
message = {
    "id": 101,
    "content": "Hey, call me at 9876543210!"
}

# Test Price Suggestor
resp_price = requests.post(url_price, json=product)
print("Price Suggestor Output:", resp_price.json())

# Test Chat Moderation
resp_chat = requests.post(url_chat, json=message)
print("Chat Moderation Output:", resp_chat.json())

