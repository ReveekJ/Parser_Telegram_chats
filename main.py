import telethon.errors
from telethon.sync import TelegramClient
import time
from config import API_ID, API_HASH, PHONE


# parsing chat once
async def once_parse(name_chat_to_parse: str):
    # append to cache all chats
    # NOT DELETE THIS
    dialogs_lst = []
    async for i in client.iter_dialogs():
        dialogs_lst.append(i)

    channel = await client.get_entity(name_chat_to_parse)
    iter_mes = [i async for i in client.iter_messages(channel)][::-1]
    # return list with telegram messages
    return iter_mes
# start func:
# with client:
#     client.loop.run_until_complete(once_parse())


# sends value to name_chat_to_send
async def send_messages(name_chat_to_send: str, value: list or tuple, show_messages=False):
    # if show_messages == True: messages send to console and to chat, else only to chat
    async for message in value:
        try:
            if str(type(message)) == "<class 'telethon.tl.patched.MessageService'>":
                continue
            await client.send_message(name_chat_to_send, message)
            if show_messages:
                print(message.text)

        except telethon.errors.FloodWaitError as e:
            print('Program sleep at', e.seconds, 'because Telegram think what do you spam')
            time.sleep(e.seconds())

        except Exception as e:
            print('Program crashed(((')
            print(e)
            print('Program continues to run)))')


client = TelegramClient(PHONE, API_ID, API_HASH)
