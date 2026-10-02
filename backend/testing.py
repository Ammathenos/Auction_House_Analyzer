import requests
from backend.auth.access_token_auth import *
from backend.core.constants_core import *
import json

# user passes
region = 'us'
realm = 'azralon'
item_name = 'Thunderfury'
host = BATTLE_NET_API_HOST_URL.format(region=region)
realm_id = 3209

params_for_item_search= {
    ':region': 'us',
    '{itemId}': '19019',
    'namespace': 'static-us',
    'locale': 'en_US'
}
region = 'us'
def debug_request():
    request = requests.get(
        BATTLE_NET_API_HOST_URL.format(region='us')+BATTLE_NET_API_ITEM_ENDPOINT.format(itemId=19019),
        headers=get_access_token(0),
        params=params_for_item_search
    )
    return request.json()

# test_auth()

# print(get_token_response())
# print(BATTLE_NET_API_HOST_NAME.format(region='us')+BATTLE_NET_API_ITEM_ENDPOINT.format(itemId=19019))

with open('visualizer.json', 'w') as f:
    json.dump(debug_request(), f, indent = 4)

item = 244625

# item_request = requests.get(
#     'https://{url}/data/wow/search/item'.format(url=host),
#     ':region': REGIONS['us']
# )

# paramns_item = {
#     ':region': 'us',
#     '{itemId}': str(item),
#     'namespace': 'static-us',
#     'locale': 'en_US'
# }

# paramns_auction = {
#     ':region': 'us',
#     '{connectedRealmId}': '3209',
#     'namespace': 'dynamic-us',
#     'locale': 'en_US'
# }

# item_id_response = requests.get(
#     'https://{url}/data/wow/item/{itemId}'.format(url=host, itemId=item),
#     headers=get_token_response(),
#     params=paramns_item
# )

# auction_item_response = requests.get(
#     'https://{url}/data/wow/connected-realm/3209/auctions'.format(url=host),
#     headers= get_token_response(),
#     params=paramns_auction
# )



# data = auction_item_response.json()

# auction_item = data['auctions']

# def get_auction_item():
#     for i in auction_item:
#         if i['item']['id'] == item:
#             print(i)
#             print('--------------------------------------')
#             # with open('visualizer.json', 'a') as f:
#             #         json.dump(data, f, indent=4)
            
# get_auction_item()

# with open('visualizer.json', 'w') as f:
#     json.dump("clean", f)
# get_auction_item()

# print(data)

# with open('visualizer_one_line.json', 'w') as f:
#     json.dump(data, f)


# your_json = '["foo", {"bar": ["baz", null, 1.0, 2]}]'
# parsed = json.loads(your_json)
# print(json.dumps(parsed, indent=4))

# with open('filename.txt', 'r') as handle:
#     parsed = json.load(handle)