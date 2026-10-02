from core.constants_core import *
import clients.battle_net_client
from auth.access_token_auth import get_access_token

def get_item(region: str, item_id: str, locale: str):

    url = (
        BATTLE_NET_API_HOST_URL.format(region=region)+
        BATTLE_NET_API_ITEM_ENDPOINT.format(itemId=item_id)
    )
    params = {
        'namespace': 'static-'+region,
        'locale': locale
    }

    return clients.battle_net_client.get(url, params)

def get_item_search(region: str, item_name: str, page: str):

    url = (
        BATTLE_NET_API_HOST_URL.format(region=region)+
        BATTLE_NET_API_ITEM_SEARCH_ENDPOINT
    )
    params = {
        'namespace': 'static-'+region,
        'name.en_US': item_name,
        'orderby': 'id',
        '_page': page,
        'access_token': get_access_token()
    }

    return clients.battle_net_client.get(url, params)