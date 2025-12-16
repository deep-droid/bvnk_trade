import pytest
import time
from quote_utils import build_quote_payload

@pytest.mark.e2e
def test_exchange_rate_fluctuates_over_time(api, wallet_map):
    fw = wallet_map["ETH"][0]["id"]
    tw = wallet_map["TRX"][0]["id"]

    payload = build_quote_payload("ETH", "TRX", fw, tw, 1)

    q1 = api.create_quote(payload)
    out1 = float(q1["amountOut"])

    time.sleep(3)  # allow rate engine to move

    q2 = api.create_quote(payload)
    out2 = float(q2["amountOut"])

    assert out1 != out2, (
        f"Expected rate fluctuation but amountOut stayed the same: {out1}"
    )
