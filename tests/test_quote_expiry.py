import pytest
import time
from src.quote_utils import build_quote_payload

@pytest.mark.e2e
@pytest.mark.slow
def test_quote_expires_if_not_accepted(api, wallet_map):
    fw = wallet_map["ETH"][0]["id"]
    tw = wallet_map["TRX"][0]["id"]

    payload = build_quote_payload("ETH", "TRX", fw, tw, 1)
    quote = api.create_quote(payload)
    uuid = quote["uuid"]

    # Wait longer than simulator expiry window (20 secs by spec)
    time.sleep(25)

    quote_after = api.get_quote(uuid)

    assert quote_after["paymentStatus"] in (
        "EXPIRED",
        "FAILED",
        "CANCELLED",
    ), f"Unexpected status: {quote_after['paymentStatus']}"
