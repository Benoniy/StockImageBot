'''
Welcome to StockImageBot
A discord bot written in Python for StockImageSharks & N0ICE
'''

import discord
import random

# ---[ Bot Setup ]---
TOKEN = "Mzg5MTMxODA0NjI5NTMyNjcz.D3p31A.DF-0TaxP_5RiCEQ5547IcCjMt9o"
BOT_PREFIX = "}"

client = discord.Client()


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Noobies")
    await client.add_roles(member, role)


@client.event
async def on_message(message):
    print(message.content)
    message_content = message.content.upper()
    # Bot should not reply to itself
    if message.author != client.user:

        # Check what command was and call appropriate function
        if BOT_PREFIX + "HELLO" in message_content:
            await client.send_message(message.channel, "working")

        # Roll dice
        elif BOT_PREFIX + "ROLL" in message_content:
            try:
                argList = message_content.split()
                await roll_dice(message, argList[1], argList[2])
            except:
                print("Error rolling dice")

        # Flip a coin
        elif BOT_PREFIX + "FLIP" in message_content:
            flip = random.randint(1, 3)
            if flip == 1:
                await client.send_message(message.channel, "Heads")
            else:
                await client.send_message(message.channel, "Tails")

        elif BOT_PREFIX + "IAM" in message_content:
            await role_assign(message)


# ---[ Bot Commands ]---

async def roll_dice(message, amount, size):
    amount = int(amount)
    size = int(size)

    if amount > 10:
        amount = 10
    if size > 100:
        size = 100

    for x in range(amount):
        i = random.randint(1, size)
        await client.send_message(message.channel, i)


async def role_assign(message):
    message_content = message.content.upper()
    arg_list = message_content.split()
    print(message.channel)
    if message.channel.name == "server_guidelines":
        temp_role = discord.utils.get(message.server.roles, name="Temp Members")
        if arg_list[1] == "18+":
            if "18-" in [y.name.lower() for y in message.author.roles]:
                role = discord.utils.get(message.server.roles, name="18-")
                await client.remove_roles(message.author, role)

            role = discord.utils.get(message.server.roles, name="18+")
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, "Over 18")
        elif arg_list[1] == "18-":
            if "18+" in [y.name.lower() for y in message.author.roles]:
                role = discord.utils.get(message.server.roles, name="18+")
                await client.remove_roles(message.author, role)
            role = discord.utils.get(message.server.roles, name="18-")
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, "Under 18")

        await client.remove_roles(message.author, discord.utils.get(message.server.roles, name="Noobies"))
        await client.add_roles(message.author, temp_role)
        await delete_all_but_one(message)


def is_me(m):
    return m.author == client.user


def is_admin(message):
    if "ze moderators" in [y.name.lower() for y in message.author.roles]:
        return False
    else:
        return True


async def delete_all_but_one(message):
    if message.channel.name == "server_guidelines":
        await client.purge_from(message.channel, limit=100, check=is_admin)



# ---[ Run Bot ]---
client.run(TOKEN)
