import pytest
import logging
from src.api import BVNKClient
from src.wallet_utils import map_wallets_by_currency

logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope="session")
def api():
    client = BVNKClient()
    client.init()
    return client

@pytest.fixture(scope="session")
def wallets(api):
    return api.list_wallets()

@pytest.fixture(scope="session")
def wallet_map(wallets):
    return map_wallets_by_currency(wallets)
