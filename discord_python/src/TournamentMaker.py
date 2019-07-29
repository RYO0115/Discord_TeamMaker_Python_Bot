
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
