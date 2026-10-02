import requests
from core.constants_core import *
from auth.access_token_auth import get_access_token


def get_commodities(region, connected_realm_id, locale):
    params = {
        ':region': region,
        'namespace': 'dynamic-'+region,
        'locale': locale
    }

    request = requests.get(
        BATTLE_NET_API_HOST_URL.format(region=region)+'/data/wow/connected-realm/{connectedRealmId}/auctions'.format(connectedRealmId=connected_realm_id),
        headers=get_access_token(),
        params=params
    )
    return request.json()