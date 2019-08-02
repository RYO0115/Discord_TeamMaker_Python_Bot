import os,sys
import time
import subprocess

COMMAND  = "python3"
SRC_NAME = "BotBase.py"

dir = os.path.abspath(__file__)
proc = subprocess.Popen([COMMAND, dir[:-len("main.py")] + SRC_NAME])
while True:
    ecode = proc.poll()
    if ecode is None:
        time.sleep(2)
    elif ecode == 0:
        print('NORMAL END')
        print('NEXT' + '-'*10)
        proc = subprocess.Popen([ COMMAND, SRC_NAME])
    else:
        print('ERROR')
        print('RESTARTING' + '='*10)
        proc = subprocess.Popen([ COMMAND, SRC_NAME])