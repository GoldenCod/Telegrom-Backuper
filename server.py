from telethon import TelegramClient, events
import asyncio
from pyfiglet import figlet_format

start = figlet_format('StarBU' font = "doh")
print(start)

api_id = 
api_hash = ""

client = TelegramClient("saver" , api_id , api_hash)

@client.on(events.NewMessage(from_users=-ID))
async def saver(event):
    await client.send_message(-ID , event.message)

client.start()
client.run_until_disconnected()

