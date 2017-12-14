import re
from html.parser import HTMLParser
from urllib import parse
from crawler.blacklist_service import BlacklistService
from domain import Url
from my_exceptions import BlacklistNotFoundError
from regex_properties import RegexProperties


class LinkFinder(HTMLParser):
    """
    This class can find new URL's on an HTML page
    """

    def __init__(self, page_url):
        super().__init__()
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attributes):
        """
        Look for the <a> tag in the HTML code
        and get the value of the href attribute.
        Check if the value matches with the RegEx
        If it does match execute the __check_blacklist method
        :param tag: the tag that is found
        :param attributes: all attributes from that tag
        :return: Nothing
        """
        if tag == 'a':
            for attribute, value in attributes:
                if attribute == 'href' and value is not None:
                    value = value.strip()
                    self.__handle_value(value)

    def __handle_value(self, value):
        """
        This method makes sure that the value will be executed by the correct methode
        :param value: value of the href attribute
        :return: nothing
        """
        if not self.__check_in_blacklist(value):
                if self.__check_absolute_url(value):
                    self.__handle_absolute_url(value)
                elif self.__check_relative_url(value):
                    self.__parse_url(value)

    @staticmethod
    def __check_in_blacklist(value):
        """
        Check if the value is in the blacklist
        If not in the blacklist parse the url.
        :param value: The url that has been found by the LinkFinder
        :return: Nothing
        """
        try:
            return BlacklistService.in_blacklist(value)
        except BlacklistNotFoundError:
            raise

    @staticmethod
    def __check_absolute_url(url):
        """
        This method will check if the given url is an absolute url
        :param url: A URL
        :return: Boolean
        """
        return re.fullmatch(RegexProperties.LinkFinder.ABSOLUTE_URL, url)

    @staticmethod
    def __check_relative_url(url):
        """
        This method will check if the given url is an absolute url
        :param url: A URL
        :return: Boolean
        """
        return re.fullmatch(RegexProperties.LinkFinder.RELATIVE_URL, url)

    def __handle_absolute_url(self, url):
        """
        This method will add http:// if the url doesn't have it.
        :param url: A URL
        :return: nothing
        """
        if not re.match('http(s:|:)//', url):
            url = "http://" + url
        self.__parse_url(url)

    def __parse_url(self, url):
        """
        This method will create a new URL object from the url and add it to the self.links set.
        :param url: a url
        :return: nothing
        """
        parsed_url = Url(parse.urljoin(self.page_url.url_string, url), self.page_url.layer + 1)
        self.links.add(parsed_url)
