from fastapi import FastAPI
from app.schemas import Transaction, FraudResult
from app.engine import evaluate_transaction

app = FastAPI(title="Fraud Check API")


@app.post("/check", response_model=FraudResult)
def check_transaction(transaction: Transaction):
    return evaluate_transaction(transaction)
