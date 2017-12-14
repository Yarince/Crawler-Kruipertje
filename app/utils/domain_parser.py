from urllib.parse import urlparse


class DomainParser(object):
    """
    The methods in this class can help with getting domain info about a url
    """

    @staticmethod
    def get_domain_name(url):
        """
        This method will split a url between all dots.
        It will return the last and second to last of the result

        Example:
        input: www.isas.han.nl
        output: han.nl
        :param url:
        :return: String
        """
        try:
            results = DomainParser.get_sub_domain_name(url).split('.')
            return results[-2] + '.' + results[-1]
        except ValueError as e:
            print('DomainParser ValueError occurred:{0}'.format(e.args))
            return ''
        except IndexError as e:
            print(e)

    @staticmethod
    def get_sub_domain_name(url):
        """
        This method wil return the sub domain of  the given domain
        :param url: a url
        :return: the subdomain
        """
        return urlparse(url).netloc
