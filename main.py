from getDirAllFilename import getDirFileName
from preheattask import preheattask
import globalVariable


dir = globalVariable.localPath
if __name__ == "__main__":
    print(dir)
    datas = getDirFileName(dir)
    print("Get to datas:",datas)
    preheatTask = {
        "urls": datas
    }
    preheattask(preheatTask)

