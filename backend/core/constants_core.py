from typing import Final

BATTLE_NET_API_HOST_URL: Final[str] = 'https://{region}.api.blizzard.com'
BATTLE_NET_API_AUCTIONS_ENDPOINT: Final[str] = '/data/wow/connected-realm/{connectedRealmId}/auctions'
BATTLE_NET_API_ITEM_ENDPOINT: Final[str] = '/data/wow/item/{itemId}'
BATTLE_NET_API_ITEM_SEARCH_ENDPOINT: Final[str] = '/data/wow/search/item'

REGIONS = ('us', 'eu', 'kr')

LOCALES = ['en_US', 'es_MX', 'pt_BR', 'de_DE', 'en_GB', 'es_ES', 'fr_FR', 'it_IT', 'ru_RU', 'ko_KR']

NAMESPACES = ['static-', 'dynamic-', 'profile-']



BATTLE_NET_API_PARAMS = {
    ':region': None,
    'namespace': None,
    'locale': None,
    '{itemId}': None,
    '{connectedRealmId}': None,

}





