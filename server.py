from telethon import TelegramClient, events
import asyncio

api_id = 
api_hash = ""

client = TelegramClient("saver" , api_id , api_hash)

@client.on(events.NewMessage(from_users=-1001576073142))
async def saver(event):
    await client.send_message(-1001773767079 , event.message)

client.start()
client.run_until_disconnected()

