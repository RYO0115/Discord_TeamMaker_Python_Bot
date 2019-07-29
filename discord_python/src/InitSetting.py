
import json
import glob
import os,sys



class INIT_SETTING():
    def __init__(self, setting_filename):
        self.token = ""
        self.serverName = ""
        self.mainChannel = ""
        self.Channel1 = ""
        self.Channel2 = ""
        self.Group1 = ""
        self.Group2 = ""
        self.setting_filename = setting_filename
        self.SRC_FILE_NAME=""
        self.LoadSetting()
        #self.SETTING_FILE_DIR=SETTING_FILE_DIR
        #self.SETTING_FILE_NAME=SETTING_FILE_NAME

    def LoadSetting(self):
        dir = os.path.abspath(__file__)
        #settingDir = dir[:-len("initSetting.py")] + self.SETTING_FILE_DIR
        #settingFileName = settingDir + self.SETTING_FILE_NAME
        settingFileName = dir[: - len("initSetting.py")]
        settingFileName += self.setting_filename
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