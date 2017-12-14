import re

from my_parser.module_handler import Module
from regex_properties import RegexProperties


class JoomlaModule(Module):
    """
    This class will search for joomla data
    """

    run_all_pages = False

    def __init__(self):
        super().__init__()

    def handle_html_data(self, data):
        """
        Calls the __search_for_joomla method
        If it returns true call the __get_joomla_theme method
        :param data: The HTML source of the current page
        :return: nothing
        """
        if self.__search_for_joomla(data):
            self.__get_joomla_theme(data)

    def __search_for_joomla(self, data):
        """
        This method will search if the current page uses joomla and add it to the attributes
        :param data: HTML code
        :return: Boolean
        """
        match = re.search(RegexProperties.Joomla.JOOMLA_SITE, data)
        if match:
            self.attributes.update({'joomla_found': True})
            return True
        else:
            self.attributes.update({'joomla_found': False})
            return False

    def __get_joomla_theme(self, data):
        """_
        This method check the joomla theme of the current page. It will than add the theme to the attributes attribute
        :param data: HTML code
        :return: nothing
        """
        match = re.search(RegexProperties.Joomla.THEME, data)
        if match:
            self.attributes.update({'joomla_theme': match.group(1)})

    def is_found(self):
        return super().is_found()
