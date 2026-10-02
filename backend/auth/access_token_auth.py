import requests
from core.configs_core import BATTLE_NET_CLIENT_ID, BATTLE_NET_CLIENT_SECRET


def get_access_token():
    token_response = requests.post(
        'https://oauth.battle.net/token',
        data={"grant_type": "client_credentials"},
        auth=(BATTLE_NET_CLIENT_ID, BATTLE_NET_CLIENT_SECRET))
    request_header = {"Authorization": f"Bearer {token_response.json()['access_token']}"}
    # request_param = token_response.json()['access_token']
    return request_header

    # if param == 0:
    #     return request_header
    # else:
    #     return request_param