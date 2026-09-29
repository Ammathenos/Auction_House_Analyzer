from fastapi import FastAPI
import requests
from auth import *
from core.config import BATTLE_NET_API_HOST_NAME

app = FastAPI()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)

paramns = {
    ':region': 'us',
    '{realmSlug}': 'azralon',
    'namespace': 'dynamic-us',
    'locale': 'en_US'
}

region = 'us'
host = BATTLE_NET_API_HOST_NAME.format(region=region)

get_item_response = requests.get(
    'https://{url}/data/wow/realm/azralon'.format(url=host),
    headers= get_token_response(),
    params=paramns
)

@app.get('/home')
def get_item():
    return get_item_response.json()
