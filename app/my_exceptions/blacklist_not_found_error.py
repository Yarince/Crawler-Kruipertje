class BlacklistNotFoundError(Exception):

    def __init__(self, message='Blacklist file could not be opened!\nCrawler stopped working'):
        self.message = message

    def __str__(self):
        return self.message
