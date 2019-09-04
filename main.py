from getDirAllFilename import getDirFileName
from preheattask import preheattask
import globalVariable
import time
import executeCommand
import logging
from globalFunc import timestampToTime

dir = globalVariable.WebsitelocalPath
lastExecuteTime = 0.0
nextExecuteInterval = 0.0
nextExecuteTime = 0.0
def preheattaskdef():
    logging.info("dir = %s",dir)
    datas = getDirFileName(dir)
    logging.info("Get to datas:%s",datas)
    preheatTask = {
        "urls": datas
    }
    preheattask(preheatTask)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] - %(asctime)s\n>\tSITE:%(module)s.%(funcName)s - %(lineno)d\n>\tMSG :%(message)s")
    while True:
        if nextExecuteInterval != 0:
            logging.info("Waiting-------------> %s <-------------Wating",nextExecuteInterval)
        time.sleep(nextExecuteInterval)
        executeCommand.websitelocaGitlCommandDef("git fetch")
        command_git_rev_parse_master = executeCommand.websitelocaGitlCommandDef("git rev-parse master")
        command_git_rev_parse_origin_master = executeCommand.websitelocaGitlCommandDef("git rev-parse origin/master")
        if command_git_rev_parse_master[0] == 0 and command_git_rev_parse_origin_master[0] ==0 :
            if executeCommand.websitelocaGitlCommandDef("git rev-parse master")[1] == executeCommand.websitelocaGitlCommandDef("git rev-parse origin/master")[1]:
                nextExecuteInterval = 60
            else:
                logging.info("|================ starting pull and preheattask... ================|")
                executeCommand.websitelocaGitlCommandDef("git pull")
                preheattaskdef()
                lastExecuteTime = time.time()
                nextExecuteInterval = 1800
        else:
            logging.critical("Execute Command Error!",
                  "command_git_rev_parse_master returnCode:",command_git_rev_parse_master[0],
                  "command_git_rev_parse_origin_master returnCode:",command_git_rev_parse_origin_master[0])
            raise RuntimeError("Execute Command Error!",
                  "command_git_rev_parse_master returnCode:",command_git_rev_parse_master[0],
                  "command_git_rev_parse_origin_master returnCode:",command_git_rev_parse_origin_master[0])
        nextExecuteTime = time.time() + nextExecuteInterval
        logging.info("\n"
                     "\t{lastExecuteTimeType:<20s}[{lastExecuteTime}]\n"
                     "\t{nextExecuteTimeType:<20s}[{nextExecuteTime}]\n"
                     "\t{nextExecuteIntervalType:<20s}[{nextExecuteInterval}]"
                     .format(lastExecuteTimeType = "lastExecuteTime",lastExecuteTime = "Never execute" if lastExecuteTime == 0.0 else timestampToTime(lastExecuteTime),
                             nextExecuteTimeType = "nextExecuteTime",nextExecuteTime = timestampToTime(nextExecuteTime),
                             nextExecuteIntervalType = "nextExecuteInterval",nextExecuteInterval = nextExecuteInterval))
        # logging.info("\n"
        #              "lastExecuteTime ==> [%s]\n"
        #              "nextExecuteTime ==> [%s]\n"
        #              "nextExecuteInterval ==> [%sM]"
        #              "",time.localtime(lastExecuteTime) ,time.localtime(nextExecuteTime) ,nextExecuteInterval/60)

