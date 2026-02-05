from app.schemas import Transaction

def high_amount_rule(tx: Transaction) -> bool:
    return tx.amount > 1000

def risky_country_rule(tx: Transaction) -> bool:
    risky_countries = {"NG", "RU", "KP"}
    return tx.country in risky_countries
