import telethon.errors
from telethon.sync import TelegramClient
import time
from config import API_ID, API_HASH, PHONE


# TODO сделать эту функцию
# def wait_new_mes(channel:str):

async def append_to_cache():
    # append to cache all chats
    # NOT DELETE THIS
    dialogs_lst = []
    async for i in client.iter_dialogs():
        dialogs_lst.append(i)


# parsing chat once
async def once_parse(name_chat_to_parse: str):
    await append_to_cache()

    channel = await client.get_entity(name_chat_to_parse)
    iter_mes = [i async for i in client.iter_messages(channel)][::-1]
    # return list with telegram messages
    return iter_mes


# start func:
# with client:
#     client.loop.run_until_complete(once_parse())


# sends value to name_chat_to_send
async def send_messages(name_chat_to_send: str, value: list or tuple, show_messages=False, show_index_messages=False):
    # if show_messages == True: messages send to console and to chat, else only to chat

    await append_to_cache()

    for message in value:
        try:
            if str(type(message)) == "<class 'telethon.tl.patched.MessageService'>":
                continue
            await client.send_message(name_chat_to_send, message)
            if show_messages:
                print(message.text)
            if show_index_messages:
                print(value.index(message))

        except telethon.errors.FloodWaitError as e:
            print('Program sleep at', e.seconds, 'because Telegram think what do you spam')
            time.sleep(e.seconds)

        except Exception as e:
            print('Program crashed(((')
            print(e)
            print('Program continues to run)))')


# async def click_button(message, name_button: str): #chat: str, index_of_message: int
#     # with client:
#     #     message = client.loop.run_until_complete(once_parse(chat))
#     #     message = message[index_of_message]
#     await message.click(text=name_button)


client = TelegramClient(PHONE, API_ID, API_HASH)
# with client:
#     client.loop.run_until_complete(click_button('GPT', -1, 'Завершить диалог'))
