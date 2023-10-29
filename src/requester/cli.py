import logging
from . import bot

def execute():
    readyLogging()
    bot.startDiscordBot()

def readyLogging():
    # ログハンドラの設定
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("{asctime} [{levelname}] {message}", style="{")
    stream_handler.setFormatter(formatter)

    # ロガーにハンドラを追加
    logging.root.addHandler(stream_handler)
    logging.root.setLevel(logging.DEBUG)


if __name__ == "__main__":
    execute()

