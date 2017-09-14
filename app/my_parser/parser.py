from queue import Queue
from my_parser.data_parser import DataParser
from persistence import HTMLServiceFactory
from persistence.parser_service import ParserServiceFactory
from properties import Properties
from utils import MyThread


class Parser:
    """
    This is the main class of the Parser.
    This class will create all threads en give those threads a job to do.
    """

    def __init__(self, html_service_type, parser_service):
        self.queue = Queue()
        self.parsed = set()
        self.html_service_type = html_service_type
        self.parser_service = parser_service
        self.is_running = False

    def __create_workers(self):
        """
        Create new threads for the parser

        :return: Nothing
        """
        for _ in range(Properties.PARSER_MAX_THREADS):
            t = MyThread(HTMLServiceFactory(self.html_service_type).get_instance(), self)
            t.start()

    def work(self, thread_name, html_service_type):
        """
        This method is assigned to threads.
        As long as there are items in the queue this method wil start crawling them.

        :param thread_name: The name of the current thread
        :param html_service_type: An instance of the HTMLService
        :return:
        """
        while True:
            url = self.queue.get()
            DataParser(url,
                       html_service_type,
                       thread_name,
                       ParserServiceFactory(self.parser_service).get_instance()).parse()
            self.parsed.add(url)
            self.queue.task_done()

    def start(self):
        """
        This method wil check if the parser is already running. If it is, it will start the parser.
        :return: Nothing
        """
        if self.is_running is False:
            self.is_running = True
            self.__create_workers()

    def add_link_to_queue(self, url):
        """
        Adds the given url to the queue
        :param url: URL object
        :return: Nothing
        """
        self.queue.put(url)
