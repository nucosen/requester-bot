import logging
from requester import bot
from os import getcwd
from decouple import AutoConfig
import sys

def execute():
    readyLogging()
    checkConfig()
    bot.startDiscordBot()


def checkConfig():
    config = AutoConfig(getcwd())
    configNames = (
        "REQBOT_DB_URI",
        "REQBOT_DB_KEY",
        "REQBOT_TOKEN",
        "REQBOT_WATCH_CHANNEL"
    )
    configs = [config(configName, default=None) for configName in configNames]
    if None in configs:
        logger = logging.getLogger(__name__)
        logger.critical("初期設定が未完了です")
        logger.critical("See also: https://bit.ly/3Gpu9TU")
        sys.exit("Error code : C00")


def readyLogging():
    # ログハンドラの設定
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "{asctime} [{levelname}] {message}", style="{")
    stream_handler.setFormatter(formatter)

    # ロガーにハンドラを追加
    logging.root.addHandler(stream_handler)
    logging.root.setLevel(logging.DEBUG)


if __name__ == "__main__":
    execute()
