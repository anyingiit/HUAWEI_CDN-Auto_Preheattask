import subprocess
import globalVariable


def websitelocaGitlCommandDef(command):
    outText = None
    returnCode = 0
    try:
        out_Bytes = subprocess.check_output(command,
                                            shell=True,
                                            cwd=globalVariable.WebsitelocaGitlPath,
                                            stderr=subprocess.STDOUT
                                            )
        outText = out_Bytes.decode('utf-8')
    except subprocess.CalledProcessError as e:
        outText = e.output
        returnCode= e.returncode
        print("Execute Command Error!","returnCode:[",returnCode,"]","output:",outText)
    print("returnCode:[",returnCode,"]","output:",outText)
    return returnCode,outText