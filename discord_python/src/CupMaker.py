
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from DrawImage import DRAW_SHAPE
from TournamentMaker import *


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
                    ds.DrawText(self.start_pos[0]+t.x,self.start_pos[1]+t.y-5,member_name_text)
            image_dir = ds.SaveImage()
            image_list.append(image_dir)
            tournament_num += 1
        return(image_list)
