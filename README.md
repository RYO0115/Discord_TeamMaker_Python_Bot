# TeamMaker
Member List Maker Bot for Discord App
こちらのブランチはチーム分け機能のみになります。

- [TeamMaker](#teammaker)
- [TeamMakerとは / What is TeamMaker](#teammaker%e3%81%a8%e3%81%af--what-is-teammaker)
- [TeamMaker使用方法 / How to use TeamMaker](#teammaker%e4%bd%bf%e7%94%a8%e6%96%b9%e6%b3%95--how-to-use-teammaker)
  - [!start](#start)
- [TeamMaker追加方法 / How to invite TeamMaker](#teammaker%e8%bf%bd%e5%8a%a0%e6%96%b9%e6%b3%95--how-to-invite-teammaker)
  - [家庭用PC(Windows, Macにてインストールする場合)](#%e5%ae%b6%e5%ba%ad%e7%94%a8pcwindows-mac%e3%81%ab%e3%81%a6%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%99%e3%82%8b%e5%a0%b4%e5%90%88)
  - [常時稼働環境の作成 / How to run this bot with raspberry pi](#%e5%b8%b8%e6%99%82%e7%a8%bc%e5%83%8d%e7%92%b0%e5%a2%83%e3%81%ae%e4%bd%9c%e6%88%90--how-to-run-this-bot-with-raspberry-pi)
- [TeamMaker全体構成 / Structure of TeamMaker](#teammaker%e5%85%a8%e4%bd%93%e6%a7%8b%e6%88%90--structure-of-teammaker)

# TeamMakerとは / What is TeamMaker
皆さん、ゲームは好きですか？

僕は大好きです。
夜な夜な友人と集まり、サッカーゲームを楽しんでいます。
そんな中、ある日あまりにも人数が集まり過ぎて、紅白戦をすることになりました。

さて、チーム分けをしよう!

...

どうやって？

結局、その場では適当なスマホアプリをインストールしましたが、何度もそれをやるのは面倒!

という個人的な理由から生まれたのがこのTeam Makerです。

TeamMakerとはボイスチャットアプリとして有名な
[Discord](https://discordapp.com/)で動かせるチーム分けBotになります。

使い方は簡単。ただ指定のボイチャチャンネルに参加する人が集まった状態で一言、 **"!start"** とコメントするだけ。
これだけで自動的にチーム分けをしてくれます。

その他にもいろいろと機能があり、今後も追加していく予定です。
まずは使用方法から見てみてください。

-----------------------------------------------------------------------------

Hello guys.

I know most of you love video games.

me?

Offcourse I love it more than you do.
Mostly the game to play with many players.

This [Discord](https://discordapp.com/) Bot named
**TeamMaker** is a bot makes you more easier
to play with your friends, and teammates.

As you send the command **"!start"** in the discord
/general message, TeamMaker will make the 2 team member list
in just a second or so.

If you want to know more about it, please move to below!

# TeamMaker使用方法 / How to use TeamMaker
現在搭載されている機能は２つのチームにランダムで分けてくれること、トーナメント表の自動作成機能です。

現在TeamMakerではなにかフォントを一つ指定する必要があります。
今は以下のリンク先にある「ほのかアンティーク角」を使わせていただいています。
[フォントリンク]http://font.gloomy.jp/honoka-antique-kaku-dl.html
## !start
すでにこのbotをサーバーに入れられている方は友達と一緒にVOICE CHANNELSにあるGeneralに参加して
から以下の画像のように **!start**と打ってください。
するとGeneralに参加したメンバを勝手に2つのチームに分けてくれます。
![start](image/start.png)


# TeamMaker追加方法 / How to invite TeamMaker
## 家庭用PC(Windows, Macにてインストールする場合)
基本的にはいろいろな[ブログ](https://www.devdungeon.com/content/make-discord-bot-python)で掲載されている情報の通り、DeveloperサイトでBotを作成したあと、
自分のサーバに追加してください。
その後、Botのtokenを取得し、TeamSetting.jsonというファイルに追記してください。
このGithubにはsampleとしてSampleSetting.jsonというファイルがSettingディレクトリに
入っていますので、その名前を変更してしてください。

```json : SampleSetting.json
{
    "F1ileName":"TeamSetting.json",
    "Token":"---your token----",
    "ServerName":"---your server---",

    "MainChannel":"General",
    "Channel1":"General",
    "Channel2":"Channel2",

    "Group1":"General",
    "Group2":"Group2"
}
```

基本的に編集が必要なのはこのファイルだけです。
頭から説明すると、
```json
{
    "FileName":"TeamSetting.json",      // この設定ファイルの名前
    "Token":"---your token---",         // ここにDiscord.comにて作成したBotへのアクセスtokenを追加してください。
    "ServerName":"---your server---",   // ここにこのbotを参加させるserverの名前を入れてください。TeamMakerはこのサーバーのみを見に行きます

    "MainChannel":"General"            // チーム分けをする際に最初に全員に入っていてもらうvoice channnelです。
}
```
ここで記載しなかったものについては現在、整備中のものですので気にしないでください。
(今、releaseとdevelopにブランチを分けています.もう少々お待ち下さい)




ここまでくれば後は簡単です。お使いのPCからコマンドで

    sudo pip install discord.py
    sudo pip install pillow

でdiscord.py、PILをインストールしたあと、

    python BotBase.py

を実行すればTeamMaker Botを起動することができます。
このTeamMaker.pyはどのディレクトリからでも実行ができます。

もし、これで実行できない場合は
* tokenが間違っていないか
* Condaなどを使わず、通常のPythonを利用する

などを試してみてください。
二個目についてはどうやらDiscord.pyがソケット通信を利用していることが原因で、
Discord.comに接続できないことがあるようです。ちなみに私はMacにAnacondaをインストールして
無事に動きましたが、あとで説明するRasbianでminicondaを入れた際にはいろいろとネットワークの設定を頑張りましたが、うまく接続させることができませんでした。

## 常時稼働環境の作成 / How to run this bot with raspberry pi
現在、私はこのbotを自分のPCからではなく、Raspberry pi 2B+にて常時稼働させています。
PCからでも問題はないのですが、PCそのものをネットワークのつながらないところに持っていくことがあったり、
また、そもそも自分のPCに常時動いてほしくないというワガママから、家の中に眠っていたRaspberry Pi を引っ張りだすことにしました。

ただ、以外と落とし穴が多く存在していたので、念の為情報を残したいと思います。

まず、目指すべき環境は、

**"Raspberry Pi + Python 3.6 ~ + Discord.py"**

になります。
本来であればminicondaなどを入れて環境を作りたいと思ったのですが、
そのせいで逆に環境構築に時間がかかるというなんとも悲しい経験をしたので、ここでは一番シンプルな方法を紹介します。

まず、RasbianのイメージをmicroSDに焼きます。
ここでRasbianをチョイスした理由は、Raspberry Piユーザとしては身近だったことと、
どうやらDiscord.pyを簡単に動かせるようだという前情報を入手したからです。

Raspbianの焼付方法はググればすぐに出てくるので今は割愛します(いずれ追加します)



# TeamMaker全体構成 / Structure of TeamMaker

現在編集中(クラス図などを勉強中)


