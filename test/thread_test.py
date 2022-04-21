# Thread testing for Gyro Averaging
# Ian Webster

# https://realpython.com/python-concurrency/
# https://realpython.com/intro-to-python-threading/

import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    # Do an operation that takes some time
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # Do some other tasks while waiting for the other function to finish
    # x.join()
    logging.info("Main    : all done")
