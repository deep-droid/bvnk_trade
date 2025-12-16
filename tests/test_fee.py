import pytest

@pytest.mark.e2e
def test_fee_is_non_negative(api, wallet_map):
    fw = wallet_map["ETH"][0]["id"]
    tw = wallet_map["TRX"][0]["id"]

    quote = api.create_quote({
        "from": "ETH",
        "to": "TRX",
        "fromWallet": fw,
        "toWallet": tw,
        "amountIn": 1,
        "payInMethod": "internal",
        "payOutMethod": "internal",
    })

    fee = float(quote.get("fee", 0))
    assert fee >= 0, f"Fee must be non-negative, got {fee}"

