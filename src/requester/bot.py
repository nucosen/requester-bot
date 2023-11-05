# NOTE : This program requires the 'message_content' intent.

import re
import discord
import logging
from decouple import config
from requests import post

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
    logger = logging.getLogger(__name__)
    if message.author == client.user:
        return

    logger.debug(f"Received message : {message.content}")
    matched = re.search(r"[a-z][a-z][0-9]+",message.content)
    if matched:
        videoId = matched.group()
        logger.info(f"Video adding to DB ... : {videoId}")
        postRequest(videoId)
        await message.channel.send(f'Video added ! : {videoId}')

def postRequest(item: str):
    url = config("REQBOT_DB_URL",default=None)
    key = config("REQBOT_DB_KEY", default=None)
    if None in (url,key):
        raise Exception(f"E00 環境変数エラー {url} {key}")
    if not re.match("^[a-z][a-z][0-9]+$", item):
        logging.getLogger(__name__).error("E01 予期せぬリクエスト {0}".format(item))
        return
    payload = {"videoId": item}
    headers = {'x-apikey': str(key), 'cache-control': "no-cache"}
    resp = post(str(url), json=payload, headers=headers)
    resp.raise_for_status()

def startDiscordBot():
    DISCORD_TOKEN = config("REQBOT_DISCORD_TOKEN",default=None)
    if DISCORD_TOKEN is None:
        raise Exception(f"E00 未設定の環境変数 {DISCORD_TOKEN}")
    client.run(str(DISCORD_TOKEN))
