import os
import sys
from parser.parse import *

def usage():
    pass

def cli():
    pass

if __name__ == "__main__":

    logger = Logger(LogLevel.DEBUG)
    logger.setFormat(defaultFileFormat)
    logger.addHandler(logger.FileHandler('log.txt'))

    logger.info("Initiating cli")

    ### Parse cmd
    option, command = parse(logger, ["-h", "-V", "add_image", "asss"])
    if (not option and not command):
        logger.error("Couldn't parse the command line")

    ## Cleanup
    logger.shutdown()


