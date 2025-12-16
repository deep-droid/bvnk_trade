import time

def build_quote_payload(from_cur, to_cur, fw, tw, amount):
    return {
        "from": from_cur,
        "to": to_cur,
        "fromWallet": fw,
        "toWallet": tw,
        "amountIn": amount,
        "amountOut": None,
        "useMaximum": False,
        "useMinimum": False,
        "reference": "pytest",
        "payInMethod": "internal",
        "payOutMethod": "internal",
    }

def wait_for_success(api, uuid, timeout=60, interval=5):
    start = time.time()
    while time.time() - start < timeout:
        q = api.get_quote(uuid)
        if q["paymentStatus"] in ("SUCCESS", "FAILED", "CANCELLED"):
            return q
        time.sleep(interval)
    return q
