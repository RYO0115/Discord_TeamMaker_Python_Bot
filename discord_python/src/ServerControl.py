
import discord # インストールした discord.py
import random

class SERVER_CONTROL():
    def __init__( self, client, serverName, BOT_NAME):
        self.client = client
        self.serverName = serverName
        self.BOT_NAME = BOT_NAME

    def GetChannelList(self):
        channelList = {}
        for server in self.client.servers:
            if server.name == self.serverName:
                for channel in server.channels:
                    channelList[channel.name] = channel
        return channelList

    def GetChannelUsers(self, channelName):
        members = []
        for server in self.client.servers:
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
        discord_members = self.GetChannelUsers(channelName)
        members = []
        for member in discord_members:
            members.append(member.name)


        listIDs = self.GetListIDs(members)

        return members, listIDs



    def GetOnlineUsers(self):
        members = []
        for server in self.client.servers:
            if server.name != self.serverName:
                continue
            for member in server.members:
                if str(member.status) == 'online' and member.name != self.BOT_NAME:
                    members.append(member.name)
            break
        return members

