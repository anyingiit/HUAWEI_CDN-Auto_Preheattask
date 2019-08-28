import os
import sys
dir = r"C:\Users\AnYing\Desktop\myblog\blog\public"
def test(path):
    if os.path.isdir :
        pathlist = os.listdir(path)
        print(pathlist)
    else:
        print("dir不是目录!")
        return -1
    try:
        for rootPath,dirList,fileList in os.walk(path):
            for file in fileList:
                print(os.path.join(rootPath,file))
                filePath = str(os.path.join(rootPath,file))
                filePath = filePath.replace(path,r"https://trustme.anyingiit.com")
                filePath = filePath.replace("\\","/")
                print("处理后链接:",filePath)
    except Exception as e:
        print("文件操作错误:",e)

if __name__ == '__main__':
    test(dir)
