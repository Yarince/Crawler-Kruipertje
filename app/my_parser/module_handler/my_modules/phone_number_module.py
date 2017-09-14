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
        self.__search_for_phone_numbers(data)

    def __search_for_phone_numbers(self, data):
        """
        This method will search if the current page contains a VAT number
        :param data: HTML code
        :return: Boolean
        """
        # Replace weird characters in string.
        for ch in [' ', '(', ')', '-', '.']:
            data = data.replace(ch, '')

        match = re.findall(RegexProperties.PhoneNumber.PHONE_NUMBER, data)
        if match:
            for number in match:
                if 'phone_numbers' not in self.attributes:
                    self.attributes.update({'phone_numbers': {'0': number}})
                elif 'phone_numbers' in self.attributes:
                    count = len(self.attributes['phone_numbers'])
                    self.attributes['phone_numbers'].update({str(count): number})

    def is_found(self):
        return super().is_found()
