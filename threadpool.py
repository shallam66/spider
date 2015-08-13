# encoding: utf-8

import Queue
import threading
import sys
import time
import urllib
import logging

class MyThread(threading.Thread):
    def __init__(self, workQueue, resultQueue, timeout=30, **kwargs):
        threading.Thread.__init__(self, kwargs=kwargs)
        self.timeout = timeout
        self.setDaemon(True)
        self.workQueue = workQueue
        self.resultQueue = resultQueue
        self.start()

    def run(self):
        while True:
            try:
                callable, args, kwargs = self.workQueue.get(timeout=self.timeout)
                res = callable(args, kwargs)
                self.resultQueue.put(res+' | '+self.getName())
            except Queue.Empty:
                break
            except:
                logging.warning('Error: %s' % str(sys.exc_info()))
                raise


class ThreadPool(object):
    def __init__(self, num_of_threads=10):
        self.workQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.threads = []
        self.__createThreadPool(num_of_threads)

    def __createThreadPool(self, num_of_threads):
        for i in range(num_of_threads):
            thread = MyThread(self.workQueue, self.resultQueue)
            self.threads.append(thread)
        print 'thread created'

    def wait_for_complete(self):
        while len(self.threads):
            thread = self.threads.pop()
            if thread.isAlive():
                thread.join()

    def add_job(self, callable, *args, **kwargs):
        print 'job added'
        self.workQueue.put((callable, args, kwargs))

