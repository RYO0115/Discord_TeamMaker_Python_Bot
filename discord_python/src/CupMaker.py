
import json
import glob
import os,sys

import enum
import math

from DrawImage import DRAW_SHAPE

# @brief トーナメント内の各ラウンドの構造体。全てプレイヤーはラウンドの中に格納されて管理される
class ROUND():
    def __init__(self,stageNum, id, members):
        self.roundID = id
        self.stageNum = stageNum
        self.parentID = 0
        self.childID = []

        # それぞれのラウンドの座標を保存
        # ここではしたの*の座標を格納
        #
        # ---|
        #    *---|
        # ---|   |
        #
        self.x = 0
        self.y = 0

        self.hasChildFlag = 0
        self.PositionSetFlag = 0
        self.SetMember(members)
        self.winner = -1
        self.player_id = -1
        self.score = ""


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
            return [child1Round, child2Round], roundID+2
        return [0], roundID

    def SetParentID(self, parentID):
        self.parentID = parentID

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        self.PositionSetFlag = 1

    def SetWinnerID(self, id, score):
        self.winner = id
        self.score = score

    def SetPlayerID(self, id):
        self.player_id = id

    def GetWinnerID(self):
        return(self.winner)

# @brief トーナメント作成用の構造体.
# ここではあくまで登録されたメンバー全員を入れたトーナメント表を作成する機能と勝ち負けの登録のみにしている。
# なので、人数が多い場合や、トーナメントを分けてあげたい場合は複数個のクラスを呼んで上げる必要がある
class TOURNAMENT_MAKER():
    def __init__(self, members):
        self.members = members
        self.tournament = []
        self.start_pos = [ 120, 30]
        # 線を描く際のオフセット値
        self.y_space = 40
        self.x_space = 50

    def CreateNormalTournament(self):
        roundID = 0
        FinalRound = ROUND(0,roundID,self.members)

        self.tournament.append(FinalRound)
        self.largestStageNum = 0

        num = 0
        while len(self.tournament) > num :
            newRounds = [0]
            newRounds, roundID = self.tournament[num].CreateChildRound(roundID)
            if len(newRounds) == 2:
                self.tournament.extend(newRounds)
            if  self.largestStageNum <  self.tournament[num].roundID:
                self.largestStageNum = self.tournament[num].roundID
            num += 1

        self.SetPosition()

    def GetLargestStageNum(self):
        return(self.largestStageNum)

    def SetFirstRoundPosition(self):
        dst_firstRound = []
        for round in self.tournament:
            if len(round.memberList) == 1:
                dst_firstRound.append(round.roundID)
        self.firstRound = []

        for name in self.members:
            for round_id in dst_firstRound:
                if name == self.tournament[round_id].memberList[0]:
                    self.firstRound.append(round_id)
                    break

        for i in range(len(self.firstRound)):
            self.tournament[self.firstRound[i]].SetPosition(self.start_pos[0], self.start_pos[1] + i * self.y_space)
            self.tournament[self.firstRound[i]].SetPlayerID(i)

    def CalcNewCenterPosition(self, roundID):
        childID = self.tournament[roundID].childID
        self.tournament[roundID].x = max([self.tournament[childID[0]].x, self.tournament[childID[1]].x]) + self.x_space
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

    def SetMatchScore(self, roundID, winnerID, score):
        self.tournament[roundID].SetWinnerID(self.firstRound[winnerID], score)


# @brief TOURNAMENT_MAKER()にメンバーを登録する前の下処理と画像作成をしてあげるクラス
# TOURNAMENT_MAKERを内包しているので、ラッパーとして勝ち負けを登録する関数などを加えている
class CUP_MAKER():
    def __init__(self, member, tournament_name):
        self.tournament = []
        self.start_pos = [-100,0]
        self.line_width = 3
        self.tournament_name = tournament_name
        self.member = member
        self.member_size_array = self.CalcTournamentNum(member)


    def CreateCupTournament(self):
        for member_size in self.member_size_array:
            self.tournament.append(TOURNAMENT_MAKER(self.member[:member_size]))
            if len(self.member) > member_size:
                self.member = self.member[member_size:]
        for i in range(len(self.tournament)):
            self.tournament[i].CreateNormalTournament()

    def CalcTournamentNum(self, member):
        list_size_array = []
        divide_num = len(member)/12
        min = 100
        divide_size = len(member)
        if divide_num >= 1 and len(member)%12 != 0:
            for i in range(6, 13):
                remain = len(member) % i
                if min > remain:
                    min = remain
                    divide_size = i
            divide_num=len(member)//divide_size
            list_size_array = [divide_size for i in range(divide_num)]
            for i in range(min):
                list_size_array[i]+=1
        else:
            list_size_array.append(len(member))
        return(list_size_array)

    def SetRoundWinner(self, tournament_num, round_id, winner_id, score):
        self.tournament[tournament_num].SetMatchScore(int(round_id), int(winner_id), score)

    def DrawTournamentImage(self):
        tournament_num = 0
        image_list = []
        for tournament in self.tournament:
            image_name = self.tournament_name + str(tournament_num)
            ds = DRAW_SHAPE(image_name)
            ds.SetFontFile("font_1_honokamarugo_1.1.ttf", size=12)
            ds.GetNewImage()
            ds.DrawText( 0, 0,self.tournament_name+str(tournament_num))
            for t in tournament.tournament:
                width = self.line_width
                if t.stageNum == 0:
                    # 決勝戦は先にラウンドがないけど横線を引きたい
                    if t.winner != -1:
                        # 勝者のいる場合は太線で描画
                        width *= 2
                    ds.DrawLine(t.x, t.y, 50 + t.x, t.y, width=width)

                if len(t.childID) > 1:
                    for child in t.childID:
                        width = self.line_width
                        if t.winner != -1:
                            # もしこのラウンドの勝者がいる場合,太さを二倍とスコアを表記
                            for member in tournament.tournament[child].memberList:
                                if member == tournament.tournament[t.winner].memberList[0]:
                                    width *= 2
                                    ds.DrawText(t.x + 20, t.y - 20, t.score)
                        # ジグザグの線を描画
                        ds.DrawZigZagYtoX(t.x, t.y, 5+tournament.tournament[child].x, tournament.tournament[child].y, width=width)
                        ds.DrawText(t.x + 5, t.y - 20, "[" + str(t.roundID) + "]")
                if len(t.memberList)==1:
                    ds.DrawRectangle(self.start_pos[0]+t.x,self.start_pos[1]+t.y - 10)
                    member_name_text = " " + str(t.player_id) + "." + t.memberList[0]
                    ds.DrawText(self.start_pos[0]+t.x,self.start_pos[1]+t.y-5,member_name_text
            image_dir = ds.SaveImage()
            image_list.append(image_dir)
            tournament_num += 1
        return(image_list)
