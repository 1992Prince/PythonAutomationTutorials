import logging

"""
logging.basicConfig(filename="..\\logs\\logfile.log",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'
                    ,level=logging.INFO)

log = logging.getLogger()

log.info("This is our first log")

"""

# creating logger utility

def getLogger():
    logging.basicConfig(filename="..\\logs\\logfile.log", format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p'
                        , level=logging.INFO)

    logger = logging.getLogger()
    return logger

#logger = getLogger()
#logger.info("This is second info")
#logger.critical("I am critical resource")



