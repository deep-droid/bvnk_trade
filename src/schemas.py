ENABLE_SCHEMA_VALIDATION = True

QUOTE_SCHEMA_KEYS = {
    "uuid", "from", "to", "amountIn", "amountOut", "paymentStatus"
}

def assert_quote_schema(quote):
    if not ENABLE_SCHEMA_VALIDATION:
        return
    missing = QUOTE_SCHEMA_KEYS - quote.keys()
    assert not missing, f"Missing quote fields: {missing}"
