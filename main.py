import discord
import requests
import json
from dotenv import load_dotenv
import os 

client = discord.Client()

    
@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('$Undo-depreso'):
        response = (requests.get('https://zenquotes.io/api/random'))
        await message.channel.send(response.json())
    

load_dotenv(os.path.join(os.getcwd(), '.env'))
SECRET_KEY = os.getenv("TOKEN")
client.run(SECRET_KEY)