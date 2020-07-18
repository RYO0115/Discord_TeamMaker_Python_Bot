
import discord # インストールした discord.py
import random

class SERVER_CONTROL():
    def __init__( self, serverName, BOT_NAME):
        self.client = discord.Client()
        self.serverName = serverName
        self.BOT_NAME = BOT_NAME

        self.discordVersionInfo = discord.__version__.split(".")
        print(self.discordVersionInfo)


    def GetDiscordClient(self):
        return(self.client)

    def GetDiscordServerList(self):
        #if self.discordVersionInfo
        servers = {}
        if self.discordVersionInfo[0] == "0":
            servers = self.client.servers
        else:
            servers = self.client.guilds

        return(servers)

    def GetSelectedChannelVoiceMembers(self, channel):
        if self.discordVersionInfo[0] == "0":
            return(channel.voice_members)
        else:
            return(channel.members)

    def GetChannelList(self):
        channelList = {}
        servers = self.GetDiscordServerList()
        for server in servers:
            if server.name == self.serverName:
                for channel in server.channels:
                    channelList[channel.name] = channel
        return channelList
        

    def GetChannelUsers(self, channelName):
        members = []
        servers = self.GetDiscordServerList()
        for server in servers:
            if server.name == self.serverName:
                for channel in server.channels:
                    if channel.name == channelName:
                        members.extend(self.GetSelectedChannelVoiceMembers(channel))
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
        servers = self.GetDiscordServerList()
        for server in servers:
            if server.name != self.serverName:
                continue
            for member in server.members:
                if str(member.status) == 'online' and member.name != self.BOT_NAME:
                    members.append(member.name)
            break
        return members

    async def SendTextMessage(self, channel, text):
        if self.discordVersionInfo[0] == "0":
            await self.client.send_message(channel, text)
        else:
            await channel.send( text)
    
    async def SendImage(self, channel, imageStrDir):
        if self.discordVersionInfo[0] == "0":
            await self.client.send_file(channel, imageStrDir)
        else:
            await channel.send(file=discord.File(imageStrDir))


