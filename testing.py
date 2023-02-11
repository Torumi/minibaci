import os
import time
from loguru import logger
import sys

if __name__ == '__main__':

    logger.remove()
    logger.add("./logs/tests.log", rotation="50 MB", backtrace=True, diagnose=True)  # Automatically rotate too big file
    logger.add(sys.stdout, colorize=True, format="<green>{time:DD HH:mm:ss}</green> <level>{message}</level>",
               level='INFO')

    import main
    path = './tests/'
    test_list = os.listdir(path)
    for file in test_list:
        with (open(path+file)) as f:
            a1_, a2_, N_ = [int(i) for i in f.readline().split(' ')]
        start = time.time()
        test_result = main.main(a1_, a2_, N_)
        end = time.time()
        logger.info(f"Filename: {file} Input: {a1_} {a2_} {N_}   Output: {test_result}    Time:{end - start}")