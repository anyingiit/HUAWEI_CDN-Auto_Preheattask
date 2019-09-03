import logging
if __name__ == '__main__':
    aa="nihao"
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] - %(asctime)s\n\tSITE:%(module)s.%(funcName)s - 5\n\tMSG :%(message)s")
    logging.warning("%s",aa)