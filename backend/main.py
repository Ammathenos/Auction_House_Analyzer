from services.item_service import *
from services.auctions_service import *
import json
# import models.auctions_model 
# from db.database_db import engine, Sessionlocal
# from sqlalchemy.orm import Session
import mysql.connector
from core.configs_core import DATABASE_PASSWORD

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd= DATABASE_PASSWORD,
    database = 'wow_auction_house_analyzer_database'
)




def clean_visualizer():
    with open('visualizer.json', 'w') as f:
        f

def debug_write_item_json():
    with open('visualizer.json', 'w') as f:
        json.dump(get_item('us', '15642', 'en_US'), f, indent = 4)

def debug_write_item_search_json():
    with open('visualizer.json', 'w', encoding='utf-8') as f:
        json.dump(get_item_search('us', '', '1')['results'][1], f, indent = 4, ensure_ascii=False)

def debug_read_json():
    x = 0
    with open('AuctionsList.json', 'r') as f:
        dictf = json.load(f)
        print('test1')
        for i in f:
            print('test2')
            x += 1
            if x == 5:
                break

# print(get_item_search('us', '', '1')['results'][1])

# debug_read_json()
clean_visualizer()
debug_write_item_search_json()



















# app = FastAPI()

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run('main:app', reload=True)

# paramns = {
#     ':region': 'us',
#     '{realmSlug}': 'azralon',
#     'namespace': 'dynamic-us',
#     'locale': 'en_US'
# }

# region = 'us'
# host = BATTLE_NET_API_HOST_NAME.format(region=region)

# get_item_response = requests.get(
#     'https://{url}/data/wow/realm/azralon'.format(url=host),
#     headers= get_token_response(),
#     params=paramns
# )

# @app.get('/home')
# def get_item():
#     return get_item_response.json()
