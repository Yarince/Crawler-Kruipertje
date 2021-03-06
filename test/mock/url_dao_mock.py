class UrlDAOMock:

    def __init__(self):
        self.queue = ['http://www.technovium.nl', 'http://www.han.nl']
        self.crawled = ['http://www.blixem.nl']

    def get_queue_urls(self):
        return self.queue

    def get_crawled_urls(self):
        return self.crawled

    @staticmethod
    def get_url(url):
        return url

    def get_urls(self):
        return self.queue
    def add_queue_url(self, url):
        self.queue.append(url)

    def remove_queue_url(self, url):
        self.queue.remove(url)
