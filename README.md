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

## 📦 Technologies

- FastAPI
- Python 3.11.8
- Pydantic
- Uvicorn

## 🚀 Getting Started

### 1. Clone and install dependencies

```bash
git clone https://github.com/HK116/fraud-check-api.git
cd fraud-check-api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements