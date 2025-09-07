import pandas as pd
import re

# Load dataset
df = pd.read_csv("dataset.csv")

# ----------------------------
# Price Suggestor Agent
# ----------------------------
def price_suggestor(product):
    base_price = product['asking_price']

    # Condition multiplier
    condition = product['condition']
    if condition == 'Like New':
        multiplier = 1.0
    elif condition == 'Good':
        multiplier = 0.9
    else:  # Fair
        multiplier = 0.7

    # Age depreciation (assume 2% per month)
    age_months = product['age_months']
    age_multiplier = max(0.3, 1 - 0.02 * age_months)

    suggested_price = base_price * multiplier * age_multiplier

    # Price range ±5%
    lower = round(suggested_price * 0.95)
    upper = round(suggested_price * 1.05)

    return {
        "product_id": product['id'],
        "suggested_price_range": f"{lower}-{upper}",
        "reasoning": f"{product['title']} ({condition}, {age_months} months old). Base: {base_price}, adjusted for condition and age."
    }

# ----------------------------
# Chat Moderation Agent
# ----------------------------
abusive_words = ["badword1", "badword2", "spamword"]  # add more if needed

def chat_moderator(message, message_id=0):
    # Check phone number
    phone = re.search(r'\b\d{10}\b', message)
    if phone:
        return {"message_id": message_id, "status": "Contains Phone Number", "reason": "Message contains a 10-digit number."}

    # Check abusive words
    for word in abusive_words:
        if word in message.lower():
            return {"message_id": message_id, "status": "Abusive", "reason": f"Message contains abusive word: {word}"}

    # Safe message
    return {"message_id": message_id, "status": "Safe", "reason": "No issues detected."}
