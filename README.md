# Resellpur AI Assistant 🛒🤖

An **AI-powered assistant** for a second-hand marketplace.  
It helps buyers and sellers with:
1. **Price Suggestion** – Fair market price estimation based on product details.  
2. **Chat Moderation** – Detects unsafe messages, spam, or phone numbers.  

---

## 🚀 Features

### 🔹 Agent 1: Price Suggestor
- Input: Product details (category, condition, age, asking price).
- Output: JSON with a **suggested price range + reasoning**.
- Factors considered:
  - Category (mobile, laptop, furniture, etc.)
  - Age of the product (months)
  - Condition (Like New / Good / Fair)
  - Asking price from dataset
- *(Optional)* Can integrate with OLX / Cashify / other platforms.

### 🔹 Agent 2: Chat Moderation
- Input: Chat message between buyer and seller.
- Output: JSON with **status** (`Safe`, `Contains Phone Number`, `Spam`, etc.) + reason.

---

## 📂 Dataset

Sample dataset (`dataset.csv`) provided:

```csv
id,title,category,brand,condition,age_months,asking_price,location
1,iPhone 12,Mobile,Apple,Good,24,35000,Mumbai
2,Redmi Note 11,Mobile,Xiaomi,Like New,8,11000,Delhi
3,OnePlus Nord 2,Mobile,OnePlus,Fair,30,15000,Bangalore ```

⚙️ Tech Stack

Python 3.13

FastAPI → API framework

Uvicorn → ASGI server

Pandas → CSV/data handling

Requests → API testing

(Optional) LLMs via HuggingFace, Ollama, or OpenAI



📦 Installation & Setup
1. Clone the repo
git clone https://github.com/vvXranjan/resellpur-ai-assistant.git
cd resellpur-ai-assistant

2. Create virtual environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run FastAPI server
uvicorn app:app --reload


Server will start at: http://127.0.0.1:8000

🧪 Testing Agents

Run the test script:

python3 test_agents.py


Example Output:

Price Suggestor Output:
{
  "product_id": 1,
  "suggested_price_range": "15561-17199",
  "reasoning": "iPhone 12 (Good, 24 months old). Base: 35000.0, adjusted for condition and age."
}

Chat Moderation Output:
{
  "message_id": 101,
  "status": "Contains Phone Number",
  "reason": "Message contains a 10-digit number."
}

📌 API Endpoints
/negotiate → Price Suggestor

POST request with product JSON → returns suggested price.

/moderate → Chat Moderation

POST request with message JSON → returns moderation result.

📝 Deliverables

Modular agent implementations (agents.py)

API exposure (app.py)

Testing script (test_agents.py)

Dataset (dataset.csv)

README.md with setup & usage instructions

🔮 Future Enhancements

Connect to OLX / Cashify APIs for real-time pricing.

Advanced LLM-based chat moderation (abuse, fraud detection).

Multi-agent negotiation bot.

Recommendation engine for buyers & sellers.
