import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is connected to the Discord')

@client.event
async def on_message(message):
    if message.content == 'çay getir':
        await message.channel.send('Çaylaaarrrr')
        await message.add_reaction('🍵')
    if message.content == 'eyvallah':
        await message.channel.send('Rica ederim afiyet olsun.')
        await message.add_reaction('☺️')

client.run(TOKEN)