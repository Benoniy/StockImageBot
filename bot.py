'''
Welcome to StockImageBot
A discord bot written in Python for StockImageSharks & N0ICE
'''

import discord
from discord.ext.commands import Bot

#---[ Bot Setup ]---
TOKEN = "EkjvWn3NWNpN3OmwwfbPN0TP6K-kk89W"
BOT_PREFIX = ''

client = discord.Client()

@client.event
async def on_message(message):
    # Bot should not reply to itself
    if message.author == client.user:
        return

    # Check what command was and call appropriate function

#---[ Bot Commands ]---

@client.command(
                #Help
                name='help',
                description="Provides help to user.",
                brief="Prints help menu",
                aliases=['h', '!'],
                pass_context=False
                )
async def help():
    await client.say("Hi I'm stock-image-bot")

#---[ Run Bot ]---
client.run(TOKEN)