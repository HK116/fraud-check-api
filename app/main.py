from fastapi import FastAPI
from app.schemas import Transaction, RuleCheckResult
from app.rules import check_rules

app = FastAPI(title="Fraude Rule Simulator API")

# POST endpoint to check a transaction for fraud
@app.post("/check_transaction", response_model=RuleCheckResult)
def check_transaction(transaction: Transaction):
    # Convert validated Pydantic model to a dictionary
    trnsn_dict = transaction.model_dump() # .dict() is deprecated
    
    # Evaluate fraud rules
    matched = check_rules(trnsn_dict)

    # Return result
    return {
        "fraud" : bool(matched),
        "matched_rules": matched
    }
