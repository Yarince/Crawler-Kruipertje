import re

from my_parser.module_handler import Module
from regex_properties import RegexProperties


class VatNumberModule(Module):
    """
    This class will search for VAT numbers
    """

    run_all_pages = True

    def __init__(self):
        super().__init__()

    def handle_html_data(self, data):
        """
        Calls the __search_for_vat_numbers method
        :param data: The HTML source of the current page
        :return: nothing
        """
        self.__search_for_vat_numbers(data)

    def __search_for_vat_numbers(self, data):
        """
        This method will search if the current page contains a VAT number
        :param data: HTML code
        :return: Boolean
        """
        for ch in [' ', '(', ')', '-', '.']:
            data = data.replace(ch, '')

        match = re.findall(RegexProperties.VATNumber.VAT_NUMBER, data)
        if match:
            for vat_number in match:
                if not 'VAT_numbers' in self.attributes:
                    self.attributes.update({'VAT_numbers': {'0': vat_number}})
                elif 'VAT_numbers' in self.attributes:
                    count = len(self.attributes['VAT_numbers'])
                    self.attributes['VAT_numbers'].update({str(count): vat_number})

    def is_found(self):
        return super().is_found()

