import json
import logging
import requests

logger = logging.getLogger(__name__)

def log_request_response(response: requests.Response):
    req = response.request

    logger.info("REQUEST %s %s", req.method, req.url)
    logger.info("REQUEST HEADERS: %s", dict(req.headers))

    if req.body:
        try:
            body = json.dumps(json.loads(req.body), indent=2)
        except Exception:
            body = req.body
        logger.info("REQUEST BODY: %s", body)

    try:
        content = response.json()
        content = json.dumps(content, indent=2)
    except Exception:
        content = response.text

    logger.info("RESPONSE STATUS: %s", response.status_code)
    logger.info("RESPONSE BODY: %s", content)

    curl = f"curl -X {req.method} '{req.url}'"
    for k, v in req.headers.items():
        curl += f" -H '{k}: {v}'"
    if req.body:
        curl += f" -d '{req.body}'"

    logger.info("CURL: %s", curl)

