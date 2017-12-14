import re

from my_parser.module_handler import Module
from regex_properties import RegexProperties


class PhoneNumberModule(Module):
    """
    This class will search for phone numbers
    """

    run_all_pages = True

    def __init__(self):
        super().__init__()

    def handle_html_data(self, data):
        """
        Calls the __search_for_phone_numbers method
        :param data: The HTML source of the current page
        :return: nothing
        """
        self.__search_numbers(data)

    def __search_numbers(self, data):

        result = self.__search_for_mobile_numbers(data) + \
            self.__search_for_company_numbers(data)

        for number in result:
            if 'phone_numbers' not in self.attributes:
                self.attributes.update({'phone_found': True, 'phone_numbers': [number]})
            elif 'phone_numbers' in self.attributes:
                if number in self.attributes.get('phone_numbers'):
                    continue
                self.attributes['phone_numbers'].append(number)
        if not result:
            self.attributes.update({'phone_found': False})

    @staticmethod
    def __search_for_mobile_numbers(data):
        """
        This method will search if the current page contains a mobile number
        :param data: HTML code
        :return: Match: found data
        """
        request = RegexProperties.PhoneNumber.START + \
            RegexProperties.PhoneNumber.MOBILE_NUMBER + \
            RegexProperties.PhoneNumber.END

        match = re.findall(request, data)
        return match

    @staticmethod
    def __search_for_company_numbers(data):
        """
        This method will search if the current page contains a company number
        :param data: HTML code
        :return: Match: found data
        """
        request = RegexProperties.PhoneNumber.START + \
            RegexProperties.PhoneNumber.COMPANY_NUMBER + \
            RegexProperties.PhoneNumber.END

        match = re.findall(request, data)
        return match

    # Deprecated since 1.0
    # @staticmethod
    # def __search_for_net_numbers(data):
    #     """
    #     This method will search if the current page contains a company number
    #     :param data: HTML code
    #     :return: Match: found data
    #     """
    #     request = RegexProperties.PhoneNumber.START + \
    #         RegexProperties.PhoneNumber.NET_NUMBER + \
    #         RegexProperties.PhoneNumber.END
    #
    #     match = re.findall(request, data)
    #     return match

    def is_found(self):
        return super().is_found()
