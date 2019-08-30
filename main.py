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
        if nextExecuteInterval != 0:
            print("Waiting-------------> ", nextExecuteInterval, " <-------------Wating")
        time.sleep(nextExecuteInterval)
        executeCommand.websitelocaGitlCommandDef("git fetch")
        command_git_rev_parse_master = executeCommand.websitelocaGitlCommandDef("git rev-parse master")
        command_git_rev_parse_origin_master = executeCommand.websitelocaGitlCommandDef("git rev-parse origin/master")
        if command_git_rev_parse_master[0] == 0 and command_git_rev_parse_origin_master[0] ==0 :
            if executeCommand.websitelocaGitlCommandDef("git rev-parse master")[1] == executeCommand.websitelocaGitlCommandDef("git rev-parse origin/master")[1]:
                nextExecuteInterval = 60
            else:
                executeCommand.websitelocaGitlCommandDef("git pull")
                preheattaskdef()
                lastExecuteTime = time.time()
                nextExecuteInterval = 1800
        else:
            print("Execute Command Error!",
                  "command_git_rev_parse_master returnCode:",command_git_rev_parse_master[0],
                  "command_git_rev_parse_origin_master returnCode:",command_git_rev_parse_origin_master)
        nextExecuteTime = time.time() + nextExecuteInterval
        print("lastExecuteTime ==> ", lastExecuteTime)
        print("nextExecuteTime ==> ", nextExecuteTime)
        print("nextExecuteInterval ==> ", nextExecuteInterval)

