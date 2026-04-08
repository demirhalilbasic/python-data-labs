import pandas as pd

fp = pd.read_csv("src/fraud_patterns.csv")
print(fp[["fraud_pattern", "transaction_count"]])

fp["fraud_pattern"] = fp["fraud_pattern"].replace({
    "card_not_present":    "CNP prevara",
    "account_takeover":    "Preuzimanje računa",
    "card_present_stolen": "Ukradena kartica",
    "friendly_fraud":      "Lažna reklamacija",
    "atm_fraud":           "ATM prevara",
    "money_laundering":    "Pranje novca",
    "identity_theft":      "Krađa identiteta"
})
print(fp[["fraud_pattern", "transaction_count"]])