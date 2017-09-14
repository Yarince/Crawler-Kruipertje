import threading

import sys

from my_exceptions import MyThreadError


class MyThread(threading.Thread):
    def __init__(self, service, des_class, bucket=None):
        self.type = des_class.__class__.__name__
        threading.Thread.__init__(self)
        self.daemon = True
        self.__service = service
        self.__des_class = des_class
        self.__event = threading.Event()
        self.bucket = bucket

    def run(self):
        try:
            while not self.__event.is_set():
                lock = threading.Lock()
                lock.acquire()
                self.__des_class.work(threading.current_thread().name, self.__service)
                lock.release()
        except MyThreadError:
            self.bucket.put(sys.exc_info())

    def stop(self):
        print(self.name, "setting event state.")
        self.__event.set()

    @property
    def name(self):
        _, number = super().name.split("-")
        return self.type + "-" + number
