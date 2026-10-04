import requests
import logging
from auth.access_token_auth import get_access_token

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

def get(endpoint: str, params: dict | None = None):
    """
    Client makes a GET request to Battle.net API endpoints

    Args:
        endpoint: Request's endpoint
        params: Parameters needed for GET request
    
    Returns:
        Data containing response from GET request in form of .json()
    """
    response = requests.get(
        endpoint,
        headers=get_access_token(),
        params=params
    )

    logging.info(
        "GET %s | status=%s | tempo=%.2fs",
        response.url,
        response.status_code,
        response.elapsed.total_seconds()
    )

    response.raise_for_status()

    return response.json()