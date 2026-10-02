import os
from dotenv import load_dotenv

load_dotenv()


BATTLE_NET_CLIENT_ID = os.getenv('BATTLE_NET_CLIENT_ID')
BATTLE_NET_CLIENT_SECRET = os.getenv('BATTLE_NET_CLIENT_SECRET')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')


