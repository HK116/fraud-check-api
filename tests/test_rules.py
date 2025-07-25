from datetime import datetime
from app.rules import check_rules

# Test Rule 1: Exceed amount threshold
def test_amount_threshold_triggered():
    trnscn= {
        "amount": 2500, # above 2000
        "ip_country": "PL",
        "billing_country": "PL",
        "timestamp": datetime(2025, 7, 25, 14, 0), # safe hour
    }
    assert "exceeded_amount_threshold" in check_rules(trnscn)

# Test Rule 2: IP mismatch
def test_ip_mismatch_triggered():
    trnscn= {
        "amount": 100,
        "ip_country": "US" ,
        "billing_country": "PL",
        "timestamp": datetime(2025, 7, 25, 14, 0),
    }
    assert "ip_country_mismatch" in check_rules(trnscn)

# Test Rule 3: Odd hour
def test_odd_hour_triggered():
    trnscn= {
        "amount": 100,
        "ip_country": "PL",
        "billing_country": "PL",
        "timestamp": datetime(2025, 7, 25, 4, 0), # 4am
    }
    assert "odd_transaction_hour" in check_rules(trnscn)

# Test when no rules match
def test_no_fraud_detected():
    trnscn= {
        "amount": 100,
        "ip_country": "PL",
        "billing_country": "PL",
        "timestamp": datetime(2025, 7, 25, 14, 0),
    }
    assert check_rules(trnscn) == []