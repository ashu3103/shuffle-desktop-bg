import os
import sys
from .logger.logger import *

def usage():
    pass

def parser():
    pass

def cli():
    pass

if __name__ == "__main__":

    ### Parse cmd
    parser()

    logger = Logger(LogLevel.DEBUG)
    logger.setFormat(defaultFileFormat)
    logger.addHandler(logger.FileHandler('log.txt'))

    logger.info("Starting the cli!")

    cli()
    ## Cleanup
    logger.shutdown()


