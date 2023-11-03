# NOTE : This program requires the 'message_content' intent.

import re
import discord
import logging
import os

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
    logger = logging.getLogger("requester.bot.on_message")
    if message.author == client.user:
        return

    logger.debug(f"Received message : {message.content}")
    matched = re.search(r"[a-z][a-z][0-9]+",message.content)
    if matched:
        videoId = matched.group()
        logger.debug(f'Video ID detected : {videoId}')
        await message.channel.send(f'Video ID detected : {videoId}')

def startDiscordBot():
    logger = logging.getLogger("requester.bot.startDiscordBot")
    # FIXME : Add tokens
    token = os.getenv('DISCORD_TOKEN')
    #token = '000000000000000000000000000000000000000000000000000000000000000000000000'
    client.run(token)
