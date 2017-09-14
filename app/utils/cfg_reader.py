import configparser


class CfgReader:
    """
    Class for easy use of the configparser module
    """

    def __init__(self, file):
        self.cfg = configparser.ConfigParser(allow_no_value=True)
        self.cfg.optionxform = str
        self.cfg.read(file)

    def get_section(self, name):
        """
        Return all keys from a section in a list
        :param name: The name of the section
        :return: List()
        """
        result = list()
        for key in self.cfg[name]:
            result.append(key.strip())
        return result
