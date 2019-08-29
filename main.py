from getDirAllFilename import getDirFileName
from preheattask import preheattask
import globalVariable
import time
import executeCommand

dir = globalVariable.WebsitelocalPath
lastExecuteTime = 0.0
nextExecuteInterval = 0.0
nextExecuteTime = 0.0

def preheattaskdef():
    print(dir)
    datas = getDirFileName(dir)
    print("Get to datas:",datas)
    preheatTask = {
        "urls": datas
    }
    preheattask(preheatTask)

if __name__ == "__main__":
    while True:
        print("Waiting-------------> ",nextExecuteInterval," <-------------Wating")
        time.sleep(nextExecuteInterval)
        if executeCommand.websitelocaGitlCommandDef("git rev-parse master")[1] == executeCommand.websitelocaGitlCommandDef("git rev-parse origin/master")[1]:
            executeCommand.websitelocaGitlCommandDef("git fetch")
            nextExecuteInterval = 60
        else:
            executeCommand.websitelocaGitlCommandDef("git pull")
            preheattaskdef()
            lastExecuteTime = time.time()
            nextExecuteInterval = 1800
        nextExecuteTime = time.time() + nextExecuteInterval
        print("lastExecuteTime ==> ", lastExecuteTime)
        print("nextExecuteTime ==> ", nextExecuteTime)
        print("nextExecuteInterval ==> ", nextExecuteInterval)