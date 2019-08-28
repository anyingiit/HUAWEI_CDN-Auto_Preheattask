from globalObj import conn

def preheattask(preheatTask):
    print("preheat urls or dirs:")
    preheattask = conn.cdn.create_preheat_task(**preheatTask)
    print(preheattask)