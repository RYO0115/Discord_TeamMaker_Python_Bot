
import json
import glob
import os,sys

import matplotlib.pyplot as plt
import enum
import math

SIDE = enum.Enum("SIDE", "middle right left")
FONT_SIZE = 15
STARTPOS = [0,100]
Y_SPACE = 10
X_SPACE = 10

sample_members = ["aaaa","bbbb","cccc","dddd","eeee","ffff"]
sample_listIDs = [0,1,2,3,4,5]

#class MEMBER_CARD():
#    def __init__(self, name, id=0):
#        self.roundID = id
#        self.x = 0
#        self.y = 0
#        self.side = SIDE.right
#        self.available = 1
#
#    def Lost(self):
#        self.available = 0
#
#    def Win(self):
#        self.available = 1
#
#    def SetPosition(self, x, y, side=SIDE.right):
#        self.x = x
#        self.y = y
#        self.side = side


class ROUND():
    def __init__(self,stageNum, id, members):
        self.roundID = id
        self.stageNum = stageNum
        self.parentID = 0
        self.childID = []
        self.x = 0
        self.y = 0
        self.hasChildFlag = 0
        self.SetMember(members)
        self.PositionSetFlag = 0


    def SetMember(self, members):
        self.memberList = members
        if len(self.memberList) == 1:
            self.hasChildFlag = 1

    def CreateChildRound(self,roundID):
        if self.hasChildFlag == 0:
            self.hasChildFlag = 1
            halfLine = int(len(self.memberList) / 2)
            child1List = self.memberList[:halfLine]
            child2List = self.memberList[halfLine:]
            newStage = self.stageNum + 1
            child1Round = ROUND(newStage, roundID+1,child1List)
            child2Round = ROUND(newStage, roundID+2,child2List)
            self.childID = [roundID+1, roundID+2]
            child1Round.SetParentID(self.parentID)
            child2Round.SetParentID(self.parentID)
            #return [child1Round, child2Round]
            return [child1Round, child2Round], roundID+2

        return [0], roundID

    def SetParentID(self, parentID):
        self.parentID = parentID

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        self.PositionSetFlag = 1



class CUP_MAKER():
    def __init__(self, members, listIDs):
        self.members = members
        self.listIDs = listIDs
        self.tournament = []

    def CreateNormalTournament(self):
        roundID = 0
        FinalRound = ROUND(0,roundID,self.members)

        self.tournament.append(FinalRound)
        self.largestStageNum = 0

        num = 0
        #for i in range(len(self.tournament)):
        while len(self.tournament) > num :
            newRounds = [0]
            newRounds, roundID = self.tournament[num].CreateChildRound(roundID)
            print(num)
            if len(newRounds) == 2:
                self.tournament.extend(newRounds)
            if  self.largestStageNum <  self.tournament[num].roundID:
                self.largestStageNum = self.tournament[num].roundID
            num += 1

        self.SetPosition()

    def SetFirstRoundPosition(self):
        firstRound = []
        for round in self.tournament:
            if len(round.memberList) == 1:
                firstRound.append(round.roundID)

        for i in range(len(firstRound)):
            self.tournament[firstRound[i]].SetPosition(STARTPOS[0], STARTPOS[1] - i * Y_SPACE)

    def CalcNewCenterPosition(self, roundID):
        childID = self.tournament[roundID].childID
        self.tournament[roundID].x = max([self.tournament[childID[0]].x, self.tournament[childID[1]].x]) + X_SPACE
        y = 0
        for id in childID:
            y += self.tournament[id].y
        self.tournament[roundID].y = int(y / 2)
        self.tournament[roundID].PositionSetFlag = 1

    def SetPosition(self):
        self.SetFirstRoundPosition()
        stageNum = self.largestStageNum
        roundList = range(len(self.tournament))
        while stageNum >= 0:
            for round in roundList:
                if self.tournament[round].stageNum == stageNum:
                    if self.tournament[round].PositionSetFlag == 0:
                        self.CalcNewCenterPosition(round)
            stageNum -= 1

    def CreateTournamentGraph(self):
        for round in self.tournament:
            if len(round.childID) == 1:
                x = round.X
                y = round.y
                #Draw Rectangle
        #plt.savefig("tournament.png")



    def DebugPrint(self):
        for i in range(len(self.tournament)):
            print("Round %d, Stage %d" % (self.tournament[i].roundID,self.tournament[i].stageNum))
            print(self.tournament[i].memberList)

    def DebugPrint2(self):
        for i in range(len(self.tournament)):
            print("Round %d, Stage %d, (x,y)=(%d,%d)" % (self.tournament[i].roundID,self.tournament[i].stageNum, self.tournament[i].x, self.tournament[i].y))
            print(self.tournament[i].memberList)

class DRAW_SHAPE():
    def __init__(self, fig, title):
        self.fig = plt.figure()
        self.fig.suptitle(title, fontsize=20, fontweight = "bold")
        self.ax = self.fig.add_subplot(1,1,1)
        self.fig.subplots_adjust(top=0.85)

    def TickParam(self, top=False, bottom=False, right=False, left=False):
        plt.tick_params(labelbottom=bottom,
                        labelleft=left,
                        labelright=right,
                        labeltop=top)

    def DrawRectangle(self, ax, x, y):


if __name__=='__main__':
    tournament = CUP_MAKER(sample_members, sample_listIDs)
    tournament.CreateNormalTournament()
    tournament.DebugPrint2()