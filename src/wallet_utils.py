#currency normalization
def normalize_currency_field(currency):
    if currency is None:
        return None
    if isinstance(currency, str):
        return currency.upper()
    if isinstance(currency, dict):
        for k in ("code", "currency", "iso", "symbol", "name"):
            v = currency.get(k)
            if isinstance(v, str):
                return v.upper()
        for v in currency.values():
            if isinstance(v, str):
                return v.upper()
    return None

def map_wallets_by_currency(wallets):
    mapping = {}
    for w in wallets:
        code = normalize_currency_field(w.get("currency"))
        if code:
            mapping.setdefault(code, []).append(w)
    return mapping

def extract_balances(wallet):
    fields = ["balance", "available", "approxBalance", "approxAvailable"]
    return {f: float(wallet.get(f, 0)) for f in fields}
