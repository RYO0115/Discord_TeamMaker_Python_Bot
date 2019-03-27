
import json
import glob
import os,sys

SETTING_FILE_DIR="/../Setting/"
SETTING_FILE_NAME="TeamSetting.json"
BOT_NAME = "TeamMaker"

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
        self.SETTING_FILE_DIR=""
        self.SETTING_FILE_NAME=""
        self.SRC_FILE_NAME=""

    def LoadSetting(self):
        dir = os.path.abspath(__file__)
        settingDir = dir[:-len("initSetting.py")] + SETTING_FILE_DIR
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