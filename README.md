
# NUCOSen/Requester-bot

[NUCOSen Broadcast](https://github.com/nucosen/broadcast) に対応するリクエスト受付Botです。

Discordのサーバーに常駐し、スラッシュコマンドでリクエストを受け付けます。

このドキュメントでは、動作の概要から運用準備、導入、起動、問題発生時のフィードバック方法、コントリビュートなどについて説明します。

## 概要

NUCOSen Broadcastにおいて、ユーザーから放送内容のリクエストを受け付けるにはリクエストデータベースへ書き込みを行う必要があります。

Requester-botを用いて、受付窓口としてDiscordをサポートしユーザーの知識レベルを問わずリクエストを受け付けるだけでなく、ユーザーのリクエスト権を容易に制限することができます。

## 導入の前提条件

Requester-botの導入前に、以下の前提条件を確認してください。

- 導入先の[Discord](https://discord.com/)サーバーにおける管理者権限が必要です。
- [NUCOSen Broadcast](https://github.com/nucosen/broadcast)が正しく設定され、特にリクエストサーバーが正常に稼働している必要があります。
- [Discord Developer Portal](https://discord.com/developers/applications)に登録し、新しいBotを作成してください。
- [Python](https://www.python.org/downloads/)のバージョン3.10以上が導入され、インターネット接続が可能なサーバーが必要です。
- このドキュメントの手順に従って導入する場合、加えて[pipを導入](https://pip.pypa.io/en/stable/getting-started/)する必要があります。

## 導入方法

### 注意事項

- Windows等の環境の場合は適宜`python`を`py`に読み替える必要があるかもしれません（未検証）。
- 複数のバージョンのPythonをインストールしている場合、`python`や`pip`は導入したいPythonのバージョンに合わせて読み替えてください。

### 手順

`<Package URL>`は[リリース](https://github.com/nucosen/requester/releases)に掲載されているパッケージのURLに読み替えてください。

```shell
pip install <Package URL>
```

インストール後、必要に応じてサーバーを再起動してください。

起動する前に、ドキュメント（準備中）に従って環境変数を設定する必要があります。

### 起動

起動方法は簡単です。`requester`コマンドを実行してください。

```shell
requester
```

ログ・エラー等は標準出力に出ます。

以下のように表示されれば、正常に稼働しています（一例）。

```log
1991-02-20 03:14:15 INFO     discord.client logging in using static token
1991-02-20 03:14:15,240 [INFO] logging in using static token
1991-02-20 03:14:17 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: 0ba5eba110000000000000000c0ffee0).
1991-02-20 03:14:17,318 [INFO] Shard ID None has connected to Gateway (Session ID: 0ba5eba110000000000000000c0ffee0).
1991-02-20 03:14:18,143 [INFO] We have logged in as Example#0000
1991-02-20 03:14:18,144 [INFO]
1991-02-20 03:14:18,145 [INFO]     _  _ _  _ ____ ____ ____ ____ _  _
1991-02-20 03:14:18,145 [INFO]     |\ | |  | |    |  | [__  |___ |\ |
1991-02-20 03:14:18,146 [INFO]     | \| |__| |___ |__| ___] |___ | \|
1991-02-20 03:14:18,146 [INFO]     ____ ____ ____    ___  ____ ___
1991-02-20 03:14:18,147 [INFO]     |__/ |___ |  | __ |__] |  |  |
1991-02-20 03:14:18,147 [INFO]     |  \ |___ |_\|    |__] |__|  |
1991-02-20 03:14:18,148 [INFO]
```

## フィードバック

Requester-botに関する質問やバグ報告、提案などのフィードバックはいつでも歓迎します。ただし、リリース前のバージョンやカスタムしたフォーク先などのバージョンはサポートできません。

**その前に：**[開発者ドキュメント](https://github.com/nucosen/requester-bot/docs/index.md)を読んだほうが早く解決するかもしれません。エラーメッセージの一覧やよくある質問などをまとめています。負担軽減にご協力ください。

- バグ報告・新機能の提案：[Issueページ](https://github.com/nucosen/requester-bot/issues)
- ご支援：[Ofuse](https://ofuse.me/sittingcat)
- その他、質問・感想など：[開発者Twitter](https://twitter.com/cuYkqv)

OfuseにIssue番号を記載していただければ、優先的に実装・対応いたします。

（支援の有無に関わらず、全てのIssueに記載された機能等の実装をお約束するものではございません。）

## 技術的支援

このリポジトリへのコントリビューションを歓迎します。以下の文書を参照してください。

- [行動規範](CODE_OF_CONDUCT.md)
- [セキュリティポリシー](SECURITY.md)
- [コントリビューションガイドライン](CONTRIBUTING.md)

## ライセンス

このプログラムはMITライセンスのもとで提供されています。詳細については、[LICENSEドキュメント](LICENSE)（英文）をご確認ください。
