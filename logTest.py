import logging
if __name__ == '__main__':
    aa=111
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s]%(asctime)s:%(message)s")
    logging.warning("%s",aa)