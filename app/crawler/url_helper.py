class URLHelper:
    """
    The method(s) in this class will help with finding url's in sets
    """

    @staticmethod
    def url_in_urlset(url, urlset):
        """
        Checks if the given url is in the given urlset
        :param url: a URL object
        :param urlset: any set/queue/list with URL objects
        :return: Boolean
        """
        for item in urlset:
            if url.url_string == item.url_string:
                return True
        return False
