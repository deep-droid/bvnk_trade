import pytest
from src.quote_utils import build_quote_payload, wait_for_success

@pytest.mark.smoke
def test_list_wallets(wallets):
    assert isinstance(wallets, list)
    assert len(wallets) > 0

@pytest.mark.smoke
def test_get_wallet(api, wallets):
    wid = wallets[0]["id"]
    wallet = api.get_wallet(wid)
    assert wallet["id"] == wid


