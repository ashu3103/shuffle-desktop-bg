import os
import sys
import stat
from parser.parse import *
from parser.options import *
from typing import List

project_directory = os.path.dirname(os.getcwd())

logger: Logger = None

def usage():
    print('usage')
    pass

def version():
    print('version')
    pass

def initiateLogger(logLevel: LogLevel, logFile: str):
    global logger 
    logger = Logger(logLevel)
    logger.setFormat(defaultFileFormat)
    if (logFile and logFile != ""):
        logger.addHandler(logger.FileHandler(logFile))
    else:
        logger.addHandler(logger.StreamHandler())

    logger.info("Initiating cli")

def destroyLogger():
    logger.shutdown()


def initiateLocalRepo(repo: str):
    ## Check if repo exists and have necessary permissions
    # if not create one with permissions (777)
    ## TODO: Think about security later
    permissions = 0o777

    if os.path.isdir(repo):
        if not (os.access(repo, os.R_OK) and os.access(repo, os.W_OK)):
            logger.error(f"Directory '{repo}' exists but doesn't have necessary permissions")
    else:
        try:
            os.mkdir(repo, mode=permissions)
            logger.debug(f"Directory '{repo}' created with permissions {oct(permissions)}")
        except OSError as e:
            logger.error(f"Error creating directory: {e}")

if __name__ == "__main__":

    """ Parse cmd arguments"""
    options: List[OptionResult]
    command: CommandResult
    options, command = parse(["--logfile=log.txt", f"--repository={os.path.join(project_directory, 'repo')}", "add_image", "asss"])
    if (not options or not command):
        usage()
        sys.exit(1)

    """ 
        Define option parameters:
        The options list returns the options provided to the script
        - The options are sorted with flaged options first and then the non-flag options
        - among those sorted options, priority ordering is also respected. for example '-h' is given higher priority than '-V'
        TODO: Add the priority in cli options
    """
    logFile = ""
    logLevel = LogLevel.DEBUG

    for option in options:
        if (option.key == 'h'):
            usage()
            sys.exit(1)
        elif (option.key == 'V'):
            version()
            sys.exit(0)
        elif (option.key == "repository" or option.key == 'r'):
            repository= option.value.argument_value
        elif (option.key == "logfile"):
            logFile = option.value.argument_value
        elif (option.key == "loglevel"):
            logLevel = option.value.argument_value
    
    initiateLogger(logLevel, logFile=logFile)
    ## Support for local repo as of now
    initiateLocalRepo(repository)

    """
        Executing a command
    """
    



    """ Cleanup """
    destroyLogger()


