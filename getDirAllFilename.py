import os
from urllib.parse import quote
import globalVariable

def getDirFileName(path):
    datas = []
    if os.path.isdir:
        pathlist = os.listdir(path)
        print(pathlist)
    else:
        print("dir不是目录!")
        return -1
    try:
        for rootPath, dirList, fileList in os.walk(path):
            for file in fileList:
                print(os.path.join(rootPath, file))
                filePath = str(os.path.join(rootPath, file)) # 获取文件完整位置


                filePath = filePath.replace(path, globalVariable.WebsiteRemoteAddress) # 将本地路径转换为博客
                filePath = filePath.replace("\\", "/") # 将 \ 转换为 /

                temp = filePath.split(":") #通过 : 把URL截断成两个部分
                filePathTrunk = {
                    "dir1": temp[0],
                    "dir2": temp[1]
                }
                filePath = filePathTrunk["dir1"] + ":" + quote(filePathTrunk["dir2"])# 通过 quote 转义https: 后面的内容
                print("处理后链接:", filePath)
                datas.append(filePath)
    except IOError as e:
        print("处理文件名时出现异常!IO流出错!",e)
    except Exception as e:
        print("处理文件名时出现异常!其他错误!", e)
    return datas
