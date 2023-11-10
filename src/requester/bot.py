# NOTE : This program requires the 'message_content' intent.

import re
import discord
import logging
from decouple import config
from requests import post
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    logger = logging.getLogger(__name__)
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
    if message.author != client.user \
            and isinstance(message.channel, discord.TextChannel) \
            and message.channel.id == int(config("REQ_WATCH_CHANNEL")):
        video = getNicoVideoFromString(message.content)
        if isinstance(video, QuotableVideo):
            postRequest(video)
            replyMessage(message, messages[SUCCESS])
        if isinstance(video, UnquotableVideo):
            replyMessage(message, messages[UNQUOTABLE])


def postRequest(item: QuotableVideo):
    headers = {
        'x-apikey': config("REQBOT_DB_KEY", cast=str),
        'cache-control': "no-cache"
    }
    resp = post(
        # NOTE - Url MUST be str.
        url=config("REQBOT_DB_URL", cast=str),  # type: ignore
        json={"videoId": item}, headers=headers
    )
    resp.raise_for_status()


def startDiscordBot():
    DISCORD_TOKEN = config("REQBOT_DISCORD_TOKEN", default=None)
    client.run(str(DISCORD_TOKEN))
