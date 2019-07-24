
import discord # インストールした discord.py
import random

import json
import glob
import os,sys

from ServerControl import *
from InitSetting import *
from CupMaker import *



class TEAM_MAKER():
    def __init__(self):
        self.members = []
        self.listIDs = []
        self.cup = []

    def update(self, members, listIDs):
        self.members = members
        self.listIDs = listIDs

    def SeparateToTeamsWithManNum(self,message, teamMemberNumStr):
        sendMessage = ""
        if len(teamMemberNumStr) == 0:
            sendMessage = "!men **MemberNum** "
            return sendMessage
        else:
            teamMemberNum = int(teamMemberNumStr)
        #channelList = GetChannelList()
        for i in range(len(self.listIDs)):
            memberNum = i % teamMemberNum
            if  memberNum == 0:
                sendMessage += "-------Group" + str(i / teamMemberNum) + "-------\n"
            sendMessage += self.members[self.listIDs[i]] + "\n"
        return sendMessage

    def SeparateToSeveralTeams(self, message, teamNumStr):
        sendMessage = ""
        if len(teamNumStr) == 0:
            sendMessage = "!teams **TeamSize** "
            return sendMessage
        else:
            teamNum = int(teamNumStr)


        teamMemberNum = len(self.members) / teamNum
        for i in range(len(self.listIDs)):
            if i % teamMemberNum == 0:
                sendMessage += "-------Group" + str(i / teamMemberNum) + "-------\n"
            sendMessage += self.members[self.listIDs[i]] + "\n"

        return sendMessage

    def SeparateTo2Teams(self,message):
        sendMessage = ""
        teamMemberNum = int(len(self.members)/2)

        for i in range(len(self.listIDs)):
            memberNum = i % teamMemberNum
            if  memberNum == 0:
                sendMessage += "-------Group"
                sendMessage += str(i / teamMemberNum)
                sendMessage += "-------\n"
            sendMessage += self.members[self.listIDs[i]]
            sendMessage += "\n"
            print(len(sendMessage))
        return sendMessage

    def CreateTournament(self, message):
        msg = message.content.split(" ")
        if len(msg) == 1:
            cup_name = "トーナメント"
        else:
            cup_name = msg[1]
        self.cup = CUP_MAKER( self.members, cup_name)
        self.cup.CreateCupTournament()
        image_list = self.cup.DrawTournamentImage()
        sendMessage = "トーナメント表作成完了"
        return sendMessage, image_list

    def SetTournamentWinner(self, message):
        sendMessage = ""
        image_list = "null"
        msg = message.content.split(" ")
        if len(msg) != 5:
            sendMessage = "勝者を設定するには以下のようにコマンドを入力してください\n !cupw トーナメント番号 ラウンド番号 買った人のID 4-2などのスコア"
        elif int(msg[1]) >= len(self.cup.tournament):
            sendMessage = "トーナメント番号が間違っています"
        #elif int(msg[1]) >= len(self.cup.tournament.tournament):
        #    sendMessage = "ラウンドの番号が間違っています"

        if sendMessage == "":
            self.cup.SetRoundWinner(int(msg[1]),int(msg[2]),int(msg[3]),msg[4])
            image_list = self.cup.DrawTournamentImage()
        return sendMessage, image_list



    def PrintTeamMember(self, teamNum):
        if len(self.members) < 2 or len(self.listIDs) < 2:
            print("Need more member!!")
            return -1

    def Print2Teams(self, message):
        groupNum = 0
        groupNumLimit = 2
        teamMemberNum = int(len(self.members)/2)
        sendMessage = ""
        for i in range(len(self.listIDs)):
            if teamMemberNum > 0:
                memberNum = i % teamMemberNum
            else:
                memberNum = i % 1

            if  memberNum == 0 and groupNum < groupNumLimit:
                indexStr = ""
                indexStr += "-------Group"
                indexStr += str(groupNum+1)
                groupNum += 1
                indexStr += "-------\n"

                #await self.client.send_message(message.channel, indexStr)
                sendMessage += indexStr

            sendMessage += self.members[self.listIDs[i]]
            sendMessage += "\n"
            #await self.client.send_message(message.channel, sendMessage)
        return sendMessage

    def PrintByTeamNum(self, message):
        messageStr = message.content.split(' ')
        if len(messageStr) == 2:
            teamNumStr = messageStr[1]
            teamNumStr = teamNumStr.replace(' ','')
            sendMessage = self.SeparateToSeveralTeams(message,teamNumStr)
        elif len(messageStr) == 1:
            sendMessage = "!teams **teamNum**"
        return sendMessage

    def PrintByMemberNum(self, message):
        messageStr = message.content.split(' ')
        if len(messageStr) == 2:
            manNumStr = messageStr[1]
            manNumStr = manNumStr.replace(' ','')
            sendMessage = self.SeparateToTeamsWithManNum(message, manNumStr)
        elif len(messageStr) == 1:
            sendMessage = "!teams **teamNum**"
        return sendMessage

    def Main( self, message):
        sendMessage = ""
        image_list = "null"
        if message.content.startswith('!start'):
            sendMessage = self.Print2Teams(message)

        elif message.content.startswith('!teams'):
            sendMessage = self.PrintByTeamNum(message)
        elif message.content.startswith('!men'):
            sendMessage = self.PrintByMemberNum(message)
        elif message.content.startswith('!cupw'):
            sendMessage,image_list = self.SetTournamentWinner(message)
        elif message.content.startswith('!cup'):
            sendMessage,image_list = self.CreateTournament(message)
        else:
            sendMessage = "ごめん。何言ってるかわからない。"

        return sendMessage, image_list
        #await self.client.send_message(message.channel, sendMessage)



client = discord.Client() # 接続に使用するオブジェクト
initInfo    = INIT_SETTING()
tm = TEAM_MAKER()


# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    sendMessage = ""
    sc      = SERVER_CONTROL(client, initInfo.serverName, BOT_NAME)
    # master version
    #members, listIDs = sc.GetMemberAndListIDs(initInfo.mainChannel)
    # develop version
    members = sc.GetOnlineUsers()
    listIDs = sc.GetListIDs(members)
    tm.update(members, listIDs)

    if message.content.startswith('/neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)
    elif message.content.startswith("!"):
        sendMessage, image_list = tm.Main(message)
        if sendMessage != "":
            await client.send_message(message.channel, sendMessage)
        if image_list != "null":
            for img in image_list:
                    #await channel.send(file= discord.File(img))
                    await client.send_file(message.channel, img)


client.run(initInfo.token)
