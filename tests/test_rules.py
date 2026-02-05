from app.schemas import Transaction
from app.engine import evaluate_transaction


def test_high_risk_transaction():
    tx = Transaction(
        transaction_id="tx1",
        user_id="user1",
        amount=2000,
        country="NG",
        timestamp="2025-01-01T10:00:00"
    )

    result = evaluate_transaction(tx)

    assert result.is_fraud is True
    assert "HIGH_AMOUNT" in result.triggered_rules
    assert "RISKY_COUNTRY" in result.triggered_rules
    assert result.risk_score == 100
