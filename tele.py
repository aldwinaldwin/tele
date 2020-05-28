import configparser
#https://core.telegram.org/api/obtaining_api_id
from telethon.sync import TelegramClient
from telethon.tl.types import UpdateEditChannelMessage, UpdateNewChannelMessage

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

api_id = config['Telegram']['api_id']
api_hash = str(config['Telegram']['api_hash'])
username = config['Telegram']['username']

async def handler(update):
    if isinstance(update, (UpdateEditChannelMessage, UpdateNewChannelMessage)):
        if update.message.message:
            print('-------------------'+str(update.message.date)+'----------------')
            print(update.message.message)
            print('------------------------------------------------------')

# Use the client in a `with` block. It calls `start/disconnect` automatically.
with TelegramClient(username, api_id, api_hash) as client:
    client.add_event_handler(handler)

    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
