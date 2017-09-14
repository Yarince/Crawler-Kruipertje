import csv
from pathlib import Path
from my_exceptions import BlacklistNotFoundError
from properties import Properties


class BlacklistService:
    """
    This class can be used to check if URL's are in the blacklist.
    """

    @staticmethod
    def in_blacklist(url):
        """
        Open the blacklist file and call __handle_csv
        :param url: the url that has been found
        :return: Boolean
        """
        if not Path(Properties.BLACKLIST_FILE).is_file():
            raise BlacklistNotFoundError
        try:
            with open(Properties.BLACKLIST_FILE, 'r') as csv_file:
                read_csv = csv.reader(csv_file, delimiter=',')
                return BlacklistService.__handle_csv(read_csv, url)
        except IOError as e:
            print("IOError in Blacklist Service: {0}".format(e))

    @staticmethod
    def __handle_csv(read_csv, url):
        """
        Loops through all items in the csv file.
        If that item is found in the url return True
        else return false
        :param read_csv: the csv file that is being read
        :param url: the found url
        :return: Boolean
        """
        try:
            for row in read_csv:
                for blacklist_url in row:
                    blacklist_url = blacklist_url.strip()
                    if blacklist_url.lower() in url.lower():
                        return True
                return False
        except AttributeError as e:
            print("AttributeError occurred: {0}".format(e))
