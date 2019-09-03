from globalObj import conn
import logging

def preheattask(preheatTask):
    logging.info("ready to cdn preheattask")
    preheattask = conn.cdn.create_preheat_task(**preheatTask)
    logging.info("preheat urls or dirs:[%s]",preheattask)