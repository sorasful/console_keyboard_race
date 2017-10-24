import threading
import os

import time


class MyThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(1):
            os.system("say hello")
            # call a function

stopFlag = threading.Event()
thread = MyThread(stopFlag)
thread.start()

# this will stop the timer
time.sleep(5)
stopFlag.set()