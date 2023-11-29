# NOTE : This program requires the 'message_content' intent.

import discord
import logging
from decouple import config
from requests import post
from .nicoVideo import NicoVideo

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

resultMessages = {
    "SUCCESS": "リクエストを送信しました！",
    "UNQUOTABLE": "その動画は生放送での引用が禁止されています。\n"
    + "別の動画をリクエストしてください"
}


# SECTION - イベント定義

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
    """メッセージ受信イベント

    受信したメッセージのうち、
        1. 自身が送信したものではなく
        2. テキストチャンネル宛に送信されたもので
        3. チャンネルIDが監視対象と一致するもの
    を処理対象とし、
    メッセージをNicoVideoオブジェクトに変換したのち、
    引用可能なものはリクエストDBに送信した上で、
    結果をリプライで送信します

    Args:
        message (discord.Message): 処理するメッセージオブジェクト
    """
    if (
        message.author != client.user
        and isinstance(message.channel, discord.TextChannel)
        and message.channel.id == int(config("REQBOT_WATCH_CHANNEL"))
    ):
        video = NicoVideo.fromUri(message.content)
        if video.isExists:
            postRequest(video)
            replyMessage(message, resultMessages["SUCCESS"])

# !SECTION - イベント定義　ここまで


def startDiscordBot():
    DISCORD_TOKEN = config("REQBOT_TOKEN", default=None)
    client.run(str(DISCORD_TOKEN))


def postRequest(item: NicoVideo):
    """リクエストをDBに送信する

    Args:
        item (NicoVideo): NicoVideoオブジェクト
    """
    headers = {
        'x-apikey': config("REQBOT_DB_KEY", cast=str),
        'cache-control': "no-cache"
    }
    resp = post(
        # NOTE - Url MUST be str.
        url=config("REQBOT_DB_URI", cast=str),  # type: ignore
        json={"videoId": str(NicoVideo)}, headers=headers
    )
    resp.raise_for_status()


def replyMessage(replyTo: discord.Message, message: str):
    """Discordのメッセージにリプライを送信します

    Args:
        replyTo (discord.Message): 返信先
        message (str): 返信内容

    Raises:
        NotImplementedError: 実装前に呼び出した場合に発出します
    """
    raise NotImplementedError()
