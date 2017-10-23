import threading
import os


def printit():
  t = threading.Timer(5.0, printit)
  t.setDaemon(True)
  t.start()
  os.system("say hello")

# printit()

import threading
import time


class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=3):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            os.system("say hello")

# ThreadingExample()

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
stopFlag.set()