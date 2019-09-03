import os
from urllib.parse import quote
import globalVariable
import logging

def getDirFileName(rootDir):
    exclude = [".git"]
    datas = []
    def localPathStrToAnYingBlogStr(localpath):
        resultPath = localpath #获取源路径
        resultPath = resultPath.replace(rootDir, globalVariable.WebsiteRemoteAddress)  # 将本地路径转换为博客
        resultPath = resultPath.replace("\\", "/")  # 将 \ 转换为 /

        temp = resultPath.split(":")  # 通过 : 把URL截断成两个部分
        filePathTrunk = {
            "dir1": temp[0],
            "dir2": temp[1]
        }
        resultPath = filePathTrunk["dir1"] + ":" + quote(filePathTrunk["dir2"])  # 通过 quote 转义https: 后面的内容
        logging.info("处理后链接:[%s]", resultPath)
        return resultPath
    def existExcludePath(target):
        for ex in exclude:
            if ex in target:
                return True
        return False
    def getDirFileNamePrivate(dir):
        try:
            for lists in os.listdir(dir):
                path = os.path.join(dir, lists)
                # print(path)
                if os.path.isdir(path):
                    if not existExcludePath(lists):#如果当前目录不是被排除目录,则进行遍历
                        getDirFileNamePrivate(path)
                    else:
                        logging.info("发现已被排除目录:[%s]",path)
                else:
                    logging.info("[%s]加入datas数组",path)
                    datas.append(localPathStrToAnYingBlogStr(path))
        except IOError as e:
            logging.warning("处理文件名时出现异常!IO流出错![%s]", e)
        except Exception as e:
            logging.warning("处理文件名时出现异常!其他错误![%s]", e)

    getDirFileNamePrivate(rootDir)
    if datas !=[]:
        return datas
    else:
        raise RuntimeError("最终返回[datas]数组为空!")