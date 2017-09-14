class Url:

    def __init__(self, url, layer=0):
        self.url_string = url
        self.layer = layer

    def __str__(self):
        return self.url_string

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        """Define a non-equality test"""
        return not self.__eq__(other)

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(tuple(sorted(self.__dict__.items())))
