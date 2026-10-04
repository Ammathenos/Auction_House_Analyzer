import requests
from core.constants_core import *
import clients.battle_net_client


def get_auctions(region, connected_realm_id, locale):

    url = (
        BATTLE_NET_API_HOST_URL.format(region=region)+
        BATTLE_NET_API_AUCTIONS_ENDPOINT.format(connectedRealmId=connected_realm_id)
    )

    params = {
        'namespace': 'dynamic-'+region,
        'locale': locale
    }
    return clients.battle_net_client.get(url, params)

#------------------------------------------------------------------------------------------------------

def get_commodities(region, locale):

    url = (
        BATTLE_NET_API_HOST_URL.format(region)+
        BATTLE_NET_API_COMMODITIES_ENDPOINT
    )

    params = {
        'namespace': 'dynamic-'.format(region),
        'locale': locale
    }
    return clients.battle_net_client.get(url, params)