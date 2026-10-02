import requests
from auth.access_token_auth import get_access_token

def get(endpoint: str, params: dict | None = None):
    response = requests.get(
        endpoint,
        headers=get_access_token(),
        params=params
    )

    response.raise_for_status()

    return response.json()