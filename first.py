import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events

api_id='2078224'
api_hash='308df43087108bcad15de19ddc48177b'
token='1631161227:AAFLg0fr6q9NWNgjMBamgzsEUA1tPoXaWRI'

#phone number
phone='+917355029488'

#create a telegram client & assign it to a variable client
client= TelegramClient('session',api_id,api_hash)

#connecting and building the session
client.connect()

#if script is running first time authorize the user
if not client.is_user_authorized():
    client.send_code_request(phone)

    #signing in client
    client.sign_in(phone,input('Enter OTP'))


try:
    #reciever user_id and access_hash
    reciever=InputPeerUser('1270159700','308df43087108bcad15de19ddc48177b')
    client.send_message(reciever,message='Cool',parse_mode='html')
except Exception as e:
    print(e)


client.disconnect()


