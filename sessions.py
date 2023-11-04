from telethon import TelegramClient
import json
import os

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "secrets.json"), "r") as secrets:
    data = json.load(secrets)
    api_id, api_hash, bot_token, lang_detect_key,phone_number = data["api_info"]["api_id"], data["api_info"]["api_hash"], \
                                                   data["api_info"]["bot_token"], data["lang_detect_info"]["api_key"], data["phone_number"]

client_max = TelegramClient('max', api_id, api_hash)





