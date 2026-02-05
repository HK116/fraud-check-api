from pydantic import BaseModel
from datetime import datetime
from typing import List

# Input model: defines the structure of an incoming transaction
class Transaction(BaseModel):
    transaction_id: str
    user_id: str
    amount: float = Field(..., gt=0)
    country: str
    timestamp: datetime

# Output model: defines what the API returns after rule evaluation
class FraudResult(BaseModel):
    transaction_id: str
    is_fraud: bool
    triggered_rules: List[str]
    risk_score: int