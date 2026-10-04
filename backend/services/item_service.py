from core.constants_core import *
import clients.battle_net_client
from auth.access_token_auth import get_access_token
from db.repositories import item_repository
import json

def get_item(region: str, item_id: str, locale: str | None = None):

    url = (
        BATTLE_NET_API_HOST_URL.format(region=region)+
        BATTLE_NET_API_ITEM_ENDPOINT.format(itemId=item_id)
    )
    params = {
        'namespace': 'static-'+region,
        'locale': locale
    }

    return clients.battle_net_client.get(url, params)

#------------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------

def get_item_classes_index(region, locale):
    url = (
        BATTLE_NET_API_HOST_URL.format(region=region)+
        BATTLE_NET_API_ITEM_CLASSES_INDEX_ENDPOINT
    )

    params = {
        'namespace': 'static-'+region,
        'locale': locale
    }

    return clients.battle_net_client.get(url, params)

#------------------------------------------------------------------------------------------------------

def get_item_class(region, item_class_id, locale):
    url = (
        BATTLE_NET_API_HOST_URL.format(region=region)+
        BATTLE_NET_API_ITEM_CLASS_ENDPOINT.format(itemClassId=item_class_id)
    )

    params = {
        'namespace': 'static-'+region,
        'locale': locale
    }

    return clients.battle_net_client.get(url, params)

#------------------------------------------------------------------------------------------------------

def get_item_subclass(region, item_class_id, item_subclass_id, locale):
    url = (
        BATTLE_NET_API_HOST_URL.format(region=region)+
        BATTLE_NET_API_ITEM_SUBCLASS_ENDPOINT.format(itemClassId=item_class_id, itemSubclassId=item_subclass_id)
    )

    params = {
        'namespace': 'static-'+region,
        'locale': locale
    }

    return clients.battle_net_client.get(url, params)

#------------------------------------------------------------------------------------------------------

def get_all_items(region: str, locale: str, save_to_db: bool):
    """
    Obtém todos os itens disponíveis através do Item Search da API do WoW.

    A consulta é dividida em blocos de até 1000 itens. O ID do último
    item de cada bloco é utilizado como limite mínimo da próxima consulta.
    """

    url = (
        BATTLE_NET_API_HOST_URL.format(region=region)+
        BATTLE_NET_API_ITEM_SEARCH_ENDPOINT
    )

    if save_to_db == True:
        starting_item = 1
        x = 0

        while starting_item < 2:
            params = {
                'namespace': f'static-{region}',
                'orderby': 'id',
                '_pageSize': 1000,
                '_page': 1,
                'id': f'[{starting_item},]',
                'locale': locale
            }

            data = clients.battle_net_client.get(url, params)

            for i in data:
                with open('visualizer.json', 'a', encoding='utf-8') as f:
                    json.dump(i['results'][x]['data']['id'], f, indent = 4, ensure_ascii=False)
                    x = x + 1
            x = 0

            starting_item = starting_item + 1

            if not data:
                break
        return

def update_items_database(region: str, locale):

    url = (
        BATTLE_NET_API_HOST_URL.format(region=region)+
        BATTLE_NET_API_ITEM_SEARCH_ENDPOINT
    )
    starting_item = 1

    while True:
        params = {
            'namespace': 'static-'+region,
            'orderby': 'id',
            '_pageSize': 1000,
            '_page': 1,
            'id': f'[{starting_item},]',
            'locale': locale
        }

        data = clients.battle_net_client.get(url, params)

        results = data.get('results', [])

        if not results:
            break

        for item in results:
            item_repository.save_item(item['data']['id'])

        starting_item = results[-1]['data']['id'] + 1


    # items = []

    # while True:
    #     params = {
    #         'namespace': f'static-{region}',
    #         'orderby': 'id',
    #         '_pageSize': 1000,
    #         '_page': 1,
    #         'id': f'[{starting_item},]',
    #         'locale': locale
    #     }

    #     data = clients.battle_net_client.get(url, params)

    #     results = data.get('results', [])

    #     if not results:
    #         break

    #     items.extend(results)

    #     last_item_id = results[-1]['data']['id']
    #     starting_item = last_item_id + 1

    # return items

