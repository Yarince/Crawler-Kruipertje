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
        match = re.findall(RegexProperties.VATNumber.VAT_NUMBER, data)
        for vat_number in match:
            if 'vat_number' not in self.attributes:
                self.attributes.update({'vat_found': True, 'vat_numbers': [vat_number]})
            elif 'vat_number' in self.attributes:
                if vat_number in self.attributes.get('vat_numbers'):
                    continue
                self.attributes['vat_numbers'].append(vat_number)
        if not match:
            self.attributes.update({'vat_found': False})

    def is_found(self):
        return super().is_found()
