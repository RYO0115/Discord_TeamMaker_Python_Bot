# TeamMaker
Member List Maker Bot for Discord App

編集中　/ Now Editing!
-------------------------

- [TeamMaker](#teammaker)
  - [編集中　/ Now Editing!](#%E7%B7%A8%E9%9B%86%E4%B8%AD--now-editing)
- [TeamMakerとは / What is TeamMaker](#teammaker%E3%81%A8%E3%81%AF--what-is-teammaker)
- [TeamMaker使用方法 / How to use TeamMaker](#teammaker%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95--how-to-use-teammaker)
  - [!start](#start)
- [TeamMaker追加方法 / How to invite TeamMaker](#teammaker%E8%BF%BD%E5%8A%A0%E6%96%B9%E6%B3%95--how-to-invite-teammaker)
- [TeamMaker全体構成 / Structure of TeamMaker](#teammaker%E5%85%A8%E4%BD%93%E6%A7%8B%E6%88%90--structure-of-teammaker)

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
現在搭載されている機能は２つのチームにランダムで分けてくれることです。
それ以外にも機能はありますが、現在デバッグ中なので、随時追加していきます。

## !start
すでにこのbotをサーバーに入れられている方は友達と一緒にVOICE CHANNELSにあるGeneralに参加して
から以下の画像のように **!start**と打ってください。
するとGeneralに参加したメンバを勝手に2つのチームに分けてくれます。
![start](image/start.png)

~~~~ 随時追記 ~~~~~

# TeamMaker追加方法 / How to invite TeamMaker
基本的にはいろいろなブログで掲載されている情報の通り、DeveloperサイトでBotを作成したあと、
自分のサーバに追加してください。
その後、Botのtokenを取得し、TeamSetting.jsonというファイルに追記してください。
このGithubにはsampleとしてSampleSetting.jsonというファイルがSettingディレクトリに
入っていますので、その名前を変更してください。
あとは、コマンドで

    sudo pip install discord.py

でdiscord.pyをインストールしたあと、

    python TeamMaker.py

を実行すれば起動することができます。



# TeamMaker全体構成 / Structure of TeamMaker

現在編集中


