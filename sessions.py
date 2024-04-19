from telethon import TelegramClient
import os

name = os.environ.get('NAME')
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

client_max = TelegramClient(name, api_id, api_hash)





