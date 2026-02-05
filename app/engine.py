from app.schemas import Transaction, FraudResult
from app import rules


def evalute_transaction(tx: Transaction) -> FraudResult:
    triggered = []

    if rules.high_amount_rule(tx):
        triggered.append("HIGH_AMOUNT")
    
    if rules.risky_country_rule(tx):
        triggered.append("RISK_COUNTRY")

    is_fraud = len(triggered) > 0
    risk_score = len(triggered) * 50

    return FraudResult(
        transaction_id=tx.transaction_id,
        is_fraud=is_fraud,
        triggered_rules=triggered,
        risk_score=risk_score
    )