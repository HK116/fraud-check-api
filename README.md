# 🚨 Fraud Rule Simulator API

A simple python API that checks transactions against predefined fraud rules using FastAPI

## 🌟 Features

- Accepts transaction data via REST API
- Evaluates fraud based on:
  - High amount threshold
  - Country mismatch
  - Suspicious hours (e.g. 2AM)
- Returns `fraud: true/false` with matched rule list
- Built with FastAPI & Pydantic
- Includes unit tests
- Docker-ready

## 📦 Technologies

- FastAPI
- Python 3.11.8
- Pydantic
- Uvicorn
- Optional: Docker

## 🚀 Getting Started

### 1. 🐍 Clone and install dependencies

```bash
git clone https://github.com/HK116/fraud-check-api.git
cd fraud-check-api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

### 2. ▶️ Run the API

```bash
unicorn app.main:app --reload
```
Visit docs: *http://localhost:8000/docs*

### 3. 💡 Example Request

POST `/check_transaction`:

```json
{
  "amount": 2500,
  "ip_country": "PL",
  "billing_country": "US",
  "timestamp": "2025-07-25T02:13:00"
}
```

Response:

```json
{
  "fraud": true,
  "matched_rules": [
    "amount_threshold",
    "ip_country_mismatch",
    "odd_transaction_hour"
  ]
}
```

### 4. 🧪 Running Tests

Install pytest if not installed:

```bash
pip insall pytest
```

Run with:

```bash
PYTHONPATH=. pytest
```

Tests live in `tests/test_rules.py` and cover:
- Amount threshold
- IP mismatch
- Odd hours
- No fraud case

### 5. 🐳 Doceker *(Optional)*

> You don't nee Docker to use or deploy this - but it's included for completeness.

📄 **Dockerfile is included**

Build and run (after installing Docker)

```bash
docker build -t fraud-api .
docker run -p 8000:8000 fraud-api
```