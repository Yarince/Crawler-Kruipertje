import hashlib


class HashService:
    """
    The methods in this class can help with hashing strings
    """

    @staticmethod
    def md5(string):
        """
        This method will hash a string and return it
        :param string:
        :return: String
        """
        m = hashlib.md5()
        m.update(string.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def num_md5(string):
        """
        This method will hash a string and then convert it to an int.
        :param string: any string to hash
        :return: int
        """
        m = HashService.md5(string)
        return int(m, base=16)
