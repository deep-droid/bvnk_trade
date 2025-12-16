import pytest

@pytest.mark.smoke
def test_echo(api):
    r = api.echo({"ping": "pong"})
    assert r["request_payload"]["ping"] == "pong"