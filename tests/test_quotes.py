import pytest
import time 
from src.quote_utils import build_quote_payload, wait_for_success
from src.schemas import assert_quote_schema

@pytest.mark.smoke
def test_create_quote(api, wallet_map):
    fw = wallet_map["ETH"][0]["id"]
    tw = wallet_map["TRX"][0]["id"]

    payload = build_quote_payload("ETH", "TRX", fw, tw, 1)
    quote = api.create_quote(payload)

    assert quote.get("uuid")
    assert_quote_schema(quote)


@pytest.mark.e2e
def test_quote_is_immutable_after_creation(api, wallet_map):
    fw = wallet_map["ETH"][0]["id"]
    tw = wallet_map["TRX"][0]["id"]

    payload = build_quote_payload("ETH", "TRX", fw, tw, 1)
    quote = api.create_quote(payload)

    uuid = quote["uuid"]

    time.sleep(5)  # wait for market to change

    refreshed = api.get_quote(uuid)

    for field in ["amountIn", "amountOut", "fee", "fromWallet", "toWallet"]:
        if field in quote:
            assert quote[field] == refreshed[field], f"{field} changed after creation"


import pytest

@pytest.mark.e2e
def test_accept_quote_only_once(api, wallet_map):
    fw = wallet_map["ETH"][0]["id"]
    tw = wallet_map["TRX"][0]["id"]

    payload = build_quote_payload("ETH", "TRX", fw, tw, 1)
    quote = api.create_quote(payload)

    uuid = quote["uuid"]

    # First quota accept
    first = api.accept_quote(uuid)
    assert first.get("paymentStatus") in ("PROCESSING", "SUCCESS")

    # Second quota accept (raw request)
    resp = api.session.put(
        f"https://bvnksimulator.pythonanywhere.com/api/v1/quote/accept/{uuid}",
        headers=api.session.headers,
    )

    assert resp.status_code == 400
    assert "Bad Request" in resp.text

    final = wait_for_success(api, uuid)
    assert final["paymentStatus"] == "SUCCESS"

