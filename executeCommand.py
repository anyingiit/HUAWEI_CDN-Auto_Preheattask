import subprocess
import globalVariable
import logging

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
        logging.critical("Execute Command[%s]Error!returnCode:[%d]output:[%s]",command,returnCode,str(outText).split("\n"))
    logging.info("returnCode:[%d],output:[%s]",returnCode,str(outText).split("\n"))
    return returnCode,outText

