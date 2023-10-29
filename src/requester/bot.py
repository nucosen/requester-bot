# NOTE : This program requires the 'message_content' intent.

import discord
import logging

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

logger = logging.getLogger("requester.bot")

@client.event
async def on_ready():
    logger.info(f'We have logged in as {client.user}')
    logo = r"""
    _  _ _  _ ____ ____ ____ ____ _  _
    |\ | |  | |    |  | [__  |___ |\ |
    | \| |__| |___ |__| ___] |___ | \|
    ____ ____ ____    ___  ____ ___
    |__/ |___ |  | __ |__] |  |  |
    |  \ |___ |_\|    |__] |__|  |
    """.splitlines()

    for l in logo:
        logger.info(l)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('https://www.nicovideo.jp/watch/'):
        await message.channel.send('Nicovideo URL detected!')

def startDiscordBot():
    logger = logging.getLogger("requester.bot.startDiscordBot")
    token = ""
    client.run(token)
