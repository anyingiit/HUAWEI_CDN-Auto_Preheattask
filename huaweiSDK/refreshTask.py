from connect import conn
import logging

def refreshTask(refreshTask):
    logging.info("ready to cdn refresh")
    refreshtask = conn.cdn.create_refresh_task(**refreshTask)
    logging.info("refreshtask urls or dirs:[%s]",refreshtask)