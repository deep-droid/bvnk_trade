import pytest
import math 
from quote_utils import build_quote_payload, wait_for_success
from wallet_utils import extract_balances

@pytest.mark.e2e
@pytest.mark.slow
@pytest.mark.parametrize(
    "from_cur,to_cur,amount,verify_fee",
    [
        # Without fee
        ("ETH", "TRX", 1, False),
        ("TRX", "USDT", 420, False),
        ("TRX", "ETH", 987, False),

        # With fee
        ("ETH", "TRX", 1, True),
        ("TRX", "USDT", 420, True),
        ("TRX", "ETH", 987, True),    ]
)

def test_trade_flow(
    api,
    wallet_map,
    from_cur,
    to_cur,
    amount,
    verify_fee
):
    fw = wallet_map[from_cur][0]["id"]
    tw = wallet_map[to_cur][0]["id"]

    before_from = extract_balances(api.get_wallet(fw))
    before_to   = extract_balances(api.get_wallet(tw))

    payload = build_quote_payload(from_cur, to_cur, fw, tw, amount)
    quote = api.create_quote(payload)
    uuid = quote["uuid"]

    api.accept_quote(uuid)
    quote = wait_for_success(api, uuid)

    assert quote["paymentStatus"] == "SUCCESS"

    after_from = extract_balances(api.get_wallet(fw))
    after_to   = extract_balances(api.get_wallet(tw))

    amount_in  = float(quote["amountIn"])
    amount_out = float(quote["amountOut"])
    fee        = float(quote.get("fee", 0))

    from_delta = after_from["balance"] - before_from["balance"]
    to_delta   = after_to["balance"] - before_to["balance"]

    expected_from = -(amount_in + fee) if verify_fee else -amount_in
    expected_to   = amount_out

    assert math.isclose(from_delta, expected_from, abs_tol=1e-6)
    assert math.isclose(to_delta, expected_to, abs_tol=1e-6)