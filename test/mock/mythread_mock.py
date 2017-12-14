class MyThreadMock:

    def __init__(self):
        pass

    @staticmethod
    def work(name, url_dao):
        return "Name: {0}, DAO: {1}".format(name, url_dao)
