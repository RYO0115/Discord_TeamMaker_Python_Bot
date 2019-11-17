
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class TEAM_MAKER():
    def __init__(self):
        self.members = []
        self.listIDs = []

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

                sendMessage += indexStr

            sendMessage += self.members[self.listIDs[i]]
            sendMessage += "\n"
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
