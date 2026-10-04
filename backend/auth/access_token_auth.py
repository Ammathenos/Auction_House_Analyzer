import requests
import logging
from core.configs_core import BATTLE_NET_CLIENT_ID, BATTLE_NET_CLIENT_SECRET


def get_access_token():
    token_response = requests.post(
        'https://oauth.battle.net/token',
        data={"grant_type": "client_credentials"},
        auth=(BATTLE_NET_CLIENT_ID, BATTLE_NET_CLIENT_SECRET))
    request_header = {"Authorization": f"Bearer {token_response.json()['access_token']}"}

    logging.info(
        "POST %s | status=%s | tempo=%.2fs",
        token_response.url,
        token_response.status_code,
        token_response.elapsed.total_seconds()
    )

    return request_header