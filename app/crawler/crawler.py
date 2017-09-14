from queue import Queue, Empty
import queue
import sys
from crawler.spider import Spider
from crawler.url_helper import URLHelper
from my_exceptions import BlacklistNotFoundError, MyThreadError
from persistence import UrlDAOFactory, HTMLServiceFactory
from properties import Properties
from utils import MyThread


class Crawler:
    """
    This is the main class of the application.
    All threads will be made and are given an assignment.
    This class will also keep the queue filled.
    """

    def __init__(self, db_type, html_service_type, parser):
        self.queue = Queue()
        self.crawled = set()
        self.db_type = db_type
        self.url_dao = UrlDAOFactory(db_type).get_instance()
        self.redis = HTMLServiceFactory(html_service_type).get_instance()
        self.parser = parser
        self.__threads = []
        self.bucket = Queue()

    def create_workers(self):
        """
        Create new threads for the crawler

        :return: Nothing
        """
        for _ in range(Properties.CRAWLER_MAX_THREADS):
            t = MyThread(UrlDAOFactory(self.db_type).get_instance(), self, self.bucket)
            self.__threads.append(t)
            t.start()

    def stop(self):
        for t in self.__threads:
            t.stop()

        print("All threads stopped working.")
        sys.exit()


    def work(self, thread_name, url_dao):
        """
        This method is assigned to threads.
        As long as there are items in the queue this method wil start crawling them.

        :param thread_name: The name of the current thread
        :param url_dao: an instance of UrlDAO
        :return: Nothing
        """
        try:
            while True:
                url = self.queue.get()
                Spider(url, thread_name, url_dao, self.redis).crawl()
                self.crawled.add(url)
                self.parser.add_link_to_queue(url)
                self.parser.start()
                self.queue.task_done()
        except BlacklistNotFoundError:
            while self.queue.unfinished_tasks > 0:
                self.queue.task_done()
            raise MyThreadError

    def start(self):
        """
        Call method create_workers and then call the crawl method to fill the queue
        :return: Nothing
        """
        self.create_workers()
        self.__crawl()

    def __crawl(self):
        """
        Check if there are items in the queue.
        If that's true show all items in the string and call __create_jobs
        :return: Nothing
        """
        self.__check_bucket_state()
        db_urls = self.url_dao.get_queue_urls()
        if len(db_urls) > 0 and len(set(db_urls) ^ self.crawled) is not 0:
            print("Crawler has {0} links in queue!".format(str(len(db_urls))))
            self.__create_jobs()

    def __create_jobs(self):
        """
        Loop through all url's in the Database and add them to the queue if that url isn't in self.crawled
        :return: nothing
        """
        for url in self.url_dao.get_queue_urls():
            if not URLHelper.url_in_urlset(url, self.crawled):
                self.queue.put(url)
        self.queue.join()
        self.__crawl()

    def __check_bucket_state(self):
        try:
            exc = self.bucket.get(block=False)
        except queue.Empty:
            pass
        else:
            exc_type, exc_obj, exc_trace = exc
            # deal with the exception
            print(exc_type, exc_obj)
            print(exc_trace)
            sys.exit()
