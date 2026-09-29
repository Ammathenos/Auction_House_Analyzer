import requests
from core.config import BATTLE_NET_CLIENT_ID, BATTLE_NET_CLIENT_SECRET


def get_token_response():
    token_response = requests.post(
        'https://oauth.battle.net/token',
        data={"grant_type": "client_credentials"},
        auth=(BATTLE_NET_CLIENT_ID, BATTLE_NET_CLIENT_SECRET))
    request_header = {"Authorization": f"Bearer {token_response.json()['access_token']}"}
    
    return request_header
