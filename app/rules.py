from datetime import datetime

# Evaluates a transaction against hardcoded fraud rules
def check_rules(transaction: dict) -> list[str]: 
    matched = []
    THRESHOLD = 2000

    # Rule 1: Amount exceeds threshold
    if transaction["amount"] > THRESHOLD:
        matched.append("exceeded_amount_threshold")

    # Rule 2: IP country mismatch with billing country
    if transaction["ip_country"] != transaction["billing_country"]:
        matched.append("ip_country_mismatch")

    # Rule 3: Transaction made at an unusual hour (before 6AM or after 10PM)
    trnsn_hour = transaction["timestamp"].hour
    if trnsn_hour < 6 or trnsn_hour > 22:
        matched.append("odd_transaction_hour")

    return matched