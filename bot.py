'''
Welcome to StockImageBot
A discord bot written in Python for StockImageSharks & N0ICE
'''

import discord

# ---[ Bot Setup ]---
TOKEN = "Mzg5MTMxODA0NjI5NTMyNjcz.D3nFgQ.mYtDdynguWacx2k81xmh9wj27Ww"
BOT_PREFIX = "}"

client = discord.Client()


@client.event
async def on_message(message):
    print(message.content)
    message_content = message.content.upper()
    # Bot should not reply to itself
    if message.author != client.user:
        # Check what command was and call appropriate function
        if BOT_PREFIX + "HELLO" in message_content:
            await message.channel.send("working")



# ---[ Bot Commands ]---

# ---[ Run Bot ]---
client.run(TOKEN)
