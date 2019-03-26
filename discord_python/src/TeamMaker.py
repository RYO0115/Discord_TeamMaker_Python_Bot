
import discord # インストールした discord.py
import random

import json
import glob
import os,sys

import matplotlib.pyplot as plt


BOT_NAME = "TeamMaker"
SETTING_FILE_DIR = "/../Setting/"
SETTING_FILE_NAME = "TeamSetting.json"

SRC_FILE_NAME = "discordbot.py"



class INIT_SETTING():
    def __init__(self):
        self.token = ""
        self.serverName = ""
        self.mainChannel = ""
        self.Channel1 = ""
        self.Channel2 = ""
        self.Group1 = ""
        self.Group2 = ""
        self.LoadSetting()

    def LoadSetting(self):
        dir = os.path.abspath(__file__)
        settingDir = dir[:-(len(SRC_FILE_NAME))] + SETTING_FILE_DIR
        settingFileName = settingDir + SETTING_FILE_NAME
        print(settingFileName)

        with open(settingFileName, "r") as fp:
            jsonSettingList = json.load(fp)
            self.token = jsonSettingList["Token"]
            self.serverName = jsonSettingList["ServerName"]
            self.mainChannel  = jsonSettingList["MainChannel"]
            self.Channel1   = jsonSettingList["Channel1"]
            self.Channel2   = jsonSettingList["Channel2"]
            self.Group1     = jsonSettingList["Group1"]
            self.Group2     = jsonSettingList["Group2"]


class SERVER_CONTROL():
    def __init__( self, client, serverName):
        self.client = client
        self.serverName = serverName

    def GetChannelList(self):
        channelList = {}
        for server in client.servers:
            if server.name == self.serverName:
                for channel in server.channels:
                    channelList[channel.name] = channel
        return channelList

    def GetChannelUsers(self, channelName):
        members = []
        for server in client.servers:
            if server.name == self.serverName:
                for channel in server.channels:
                    if channel.name == channelName:
                        for member in channel.voice_members:
                            members.append(member)
        return members

    def GetListIDs(self, members):
        memberListSize = len(members)
        listIDs = list(range(memberListSize))
        random.shuffle(listIDs)
        return listIDs

    def GetMemberAndListIDs(self, channelName):
        members = self.GetChannelUsers(channelName)
        listIDs = self.GetListIDs(members)

        return members, listIDs



    def GetOnlineUsers(self):
        members = []
        for server in self.client.servers:
            if server.name != self.serverName:
                continue
            for member in server.members:
                if str(member.status) == 'online' and member.name != BOT_NAME:
                    members.append(member)
            break
        return members



class TEAM_MAKER():
    def __init__(self, members, listIDs):
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
            sendMessage += self.members[self.listIDs[i]].name + "\n"
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
            sendMessage += self.members[self.listIDs[i]].name + "\n"

        return sendMessage

    def SeparateTo2Teams(self,message):
        sendMessage = ""
        #members = GetChannelUsers(Group1)
        #channelList = GetChannelList()

        teamMemberNum = int(len(self.members)/2)


        for i in range(len(self.listIDs)):
            memberNum = i % teamMemberNum
            if  memberNum == 0:
                sendMessage += "-------Group"
                sendMessage += str(i / teamMemberNum)
                sendMessage += "-------\n"
            sendMessage += self.members[self.listIDs[i]].name
            sendMessage += "\n"
            print(len(sendMessage))
        return sendMessage

    def PrintTeamMember(self, teamNum):
        if len(self.members) < 2 or len(self.listIDs) < 2:
            print("Need more member!!")
            return -1

client = discord.Client() # 接続に使用するオブジェクト
initInfo    = INIT_SETTING()


# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    sc      = SERVER_CONTROL(client, initInfo.serverName)
    members, listIDs = sc.GetMemberAndListIDs(initInfo.mainChannel)
    tm      = TEAM_MAKER(members, listIDs)
    sendMessage = ""
    if message.content.startswith('/neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)

    elif message.content.startswith('!start'):
        print("start")
        ##members = GetOnlineUsers()
        #members = GetChannelUsers("General")
        ##channelList = GetChannelList()
        #listIDs = GetListIDs()
        #print(members)

        teamMemberNum = int(len(members)/2)
        print(teamMemberNum)

        groupNum = 0
        groupNumLimit = 2
        for i in range(len(listIDs)):
            sendMessage = ""
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
                await client.send_message(message.channel, indexStr)
            sendMessage += members[listIDs[i]].name
            sendMessage += "\n"
            await client.send_message(message.channel, sendMessage)
        #sendMessage = SeparateTo2Teams(message)

    elif message.content.startswith('!teams'):
        messageStr = message.content.split(' ')
        if len(messageStr) == 2:
            teamNumStr = messageStr[1]
            teamNumStr = teamNumStr.replace(' ','')
            sendMessage = tm.SeparateToSeveralTeams(message,teamNumStr)
        elif len(messageStr) == 1:
            sendMessage = "!teams **teamNum**"

    elif message.content.startswith('!men'):
        messageStr = message.content.split(' ')
        if len(messageStr) == 2:
            manNumStr = messageStr[1]
            manNumStr = teamNumStr.replace(' ','')
            sendMessage = tm.SeparateToTeamsWithManNum(message, manNumStr)
        elif len(messageStr) == 1:
            sendMessage = "!teams **teamNum**"

    #print(sendMessage)
    #if sendMessage != "":
    #    await client.send_message(message.channel, sendMessage)

client.run(initInfo.token)
