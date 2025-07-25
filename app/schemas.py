from pydantic import BaseModel
from datetime import datetime

# Input model: defines the structure of an incoming transaction
class Transaction(BaseModel):
    amount: float
    ip_country: str
    billing_country: str
    timestamp: datetime

# Output model: defines what the API returns after rule evaluation
class RuleCheckResult(BaseModel):
    fraud: bool
    matched_rules: list[str]