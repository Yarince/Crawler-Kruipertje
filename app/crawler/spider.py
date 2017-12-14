import socket
import ssl
import time
from collections import deque
from http.client import BadStatusLine, IncompleteRead
from urllib import request as req
from urllib.parse import urlsplit, urlunsplit
from crawler.link_finder import LinkFinder
from crawler.url_helper import URLHelper
from enums.log import LOG
from properties import Properties
from utils import DomainParser, HashService, MyLogger, Config


class Spider:
    """
    A class for getting all urls of a page.
    The class will save url's with a new domain to the database and save the html of the current page to Redis.
    """
    TIMEOUT_TIME = 2

    def __init__(self, base_url, name, url_dao, redis):
        self.url_dao = url_dao
        self.redis = redis
        self.domain_name = DomainParser.get_domain_name(base_url.url_string)
        self.base_url = base_url
        self.deque = deque()
        self.crawled = set()
        self.deque.append(base_url)
        self.name = name

    def run(self):
        """
        Check if the queue is bigger than 0
        If it is execute __crawl_page
        :return: Nothing
        """
        # get url from queue
        while len(self.deque) > 0:
            url = self.deque.popleft()
            self.__crawl_page(url)

    def __crawl_page(self, url):
        """
        This method is the main method of the spider class.
        If the layer of the url or the size of crawled is bigger than it's corresponding property the program
        will clear the queue.
        If it's not it wil start crawling the page by opening a request and getting the html.
        It'll then save the html to redis.
        After that it'll gather all links from that page and add those links to the queue.

        :param url: URL object
        :return: nothing
        """
        start_time = time.time()
        # Check if url is already crawled or max depth of urls is not exceeded
        if url.layer > Properties.SPIDER_MAX_DEPTH \
                or len(self.crawled) > Properties.SPIDER_MAX_PAGES:
            self.deque.clear()
        else:
            try:
                request = self.__get_request(url)
                html = self.__get_html(request)
                if len(html) > 0:
                    self.__save_html_to_redis(html)
                    self.__add_links_to_queue(Spider.__gather_links(url, html))
                self.crawled.add(url)
                print(self.name, "is now crawling {}\n\t\t\t\t\t\t Queue {} | Crawled {} | Layer: {} | Duration: {}"
                      .format(str(url),
                              str(len(self.deque)),
                              str(len(self.crawled)),
                              str(url.layer),
                              time.time() - start_time))
            except req.HTTPError as e:
                MyLogger.log(LOG.SPIDER, "HTTP Error occurred [{0}]: {1} {2}".format(str(e.code), e.filename, e.reason))
            except req.URLError as e:
                MyLogger.log(LOG.SPIDER, "URL Error occurred: {0}".format(e.reason))
            except ssl.SSLError as e:
                MyLogger.log(LOG.SPIDER, "SSL Error occurred: {0}".format(e))
            except socket.timeout as e:
                MyLogger.log(LOG.SPIDER, "Timeout occurred: {0}".format(e))

    @staticmethod
    def __gather_links(page_url, html):
        """
        Creates a new LinkFinder instance with the page_url.
        LinkFinder takes html as input and returns all links found.
        :param page_url: the page_url of the page that is being crawled
        :param html: the HTML source code of the page_url
        :return: page_links, a set of URL objects
        """

        finder = LinkFinder(page_url)
        finder.feed(html)
        return finder.links

    @staticmethod
    def __get_request(page_url):
        """
        This method will return an Request object for the given page_url.
        :param page_url: the url of the request
        :return: Request
        """
        return req.Request(page_url.url_string, data=None, headers=Properties.REQUEST_HEADER)

    def __get_html(self, request):
        """
        This method will return the HTML of the request.
        :param request: Request object
        :return: The HTML of the request object
        """
        html_string = ''
        try:
            response = req.urlopen(request, timeout=self.TIMEOUT_TIME)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8").strip()
        except UnicodeDecodeError as e:
            MyLogger.log(LOG.SPIDER, "UnicodeDecodeError occurred: {0}".format(e))
        except socket.timeout as e:
            MyLogger.log(LOG.SPIDER, "Timeout occurred: {0}".format(e))
        except ConnectionResetError as e:
            MyLogger.log(LOG.SPIDER, "ConnectionResetError occurred [{0}]: {1}".format(str(e.errno), e.strerror))
        except ssl.CertificateError as e:
            MyLogger.log(LOG.SPIDER, "SSL CertificateError: {0}".format(e.args))
        except BadStatusLine as e:
            MyLogger.log(LOG.SPIDER, "BadStatusLine: {0}".format(e.args))
        except IncompleteRead as e:
            MyLogger.log(LOG.SPIDER, "IncompleteRead: {0}".format(e.args))
        return html_string

    def __add_links_to_queue(self, links):
        """
        This method will loop through all URL objects in the links param.
        It will check each URL if it is already in the queue or crawled set.
        It will also check if url is from a separate domain.
        If it is then it will call the method __handle_new_domain()
        If both statements are false it will add the url to the queue
        :param links: set with URL objects
        :return: nothing
        """
        for url in links:
            # check if you want to add this url
            if URLHelper.url_in_urlset(url, self.deque) or URLHelper.url_in_urlset(url, self.crawled):
                continue
            if self.domain_name != DomainParser.get_domain_name(url.url_string):
                self.__handle_new_domain(url)
                continue
            self.deque.append(url)

    def __handle_new_domain(self, url):
        """
        This method will make a URL ready to add it to the db.
        It will also check if the url is already in the db
        :param url: the url that has been found and flagged as new domain.
        :return: nothing
        """
        split = urlsplit(url.url_string)
        clean_url = urlunsplit((split.scheme, split.netloc, "", "", ""))
        shortened_url = DomainParser.get_domain_name(clean_url)

        # Check if url is already in database

        if str(HashService.md5(shortened_url)).upper() not in Config.urls:
            self.url_dao.add_queue_url(clean_url, shortened_url)
            Config.urls.add(str(HashService.md5(shortened_url)).upper())

    def __save_html_to_redis(self, html):
        """
        Adds the html to redis using the hashed url as the key
        :param html: the value of the storage
        :return: nothing
        """
        redis_url = HashService.num_md5(self.domain_name)
        self.redis.set_list_value(redis_url, html, Properties.REDIS_KEY_EXPIRE_TIME)
