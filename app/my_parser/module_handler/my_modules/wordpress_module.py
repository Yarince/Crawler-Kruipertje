import re

from my_parser.module_handler import Module
from regex_properties import RegexProperties


class WordPressModule(Module):
    """
    This class will search for wordpress data
    """

    run_all_pages = False

    def __init__(self):
        super().__init__()

    def handle_html_data(self, data):
        """
        Calls the __search_for_wordpress method
        If it returns true call the __get_wordpress_version method
        :param data: The HTML source of the current page
        :return: nothing
        """
        if self.__search_for_wordpress(data):
            self.__get_wordpress_version(data)

    def __search_for_wordpress(self, data):
        """
        This method will search if the current page uses wordpress
        :param data: HTML code
        :return: Boolean
        """
        match = re.search(RegexProperties.WordPress.THEME, data)
        if match:
            self.attributes.update({'wordpress': True, 'wordpress_theme': match.group(1)})
            return True
        return False

    def __get_wordpress_version(self, data):
        """
        This method check the wordpress version of the current page. It will than add the version to the attributes attribute
        :param data: HTML code
        :return: nothing
        """
        match = re.search(RegexProperties.WordPress.VERSION, data)
        if match:
            self.attributes.update({'wordpress_version': match.group(1)})

    def error(self, message):
        # TODO custom exception
        raise Exception(message)

    def is_found(self):
        return super().is_found()

