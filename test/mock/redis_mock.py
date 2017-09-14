from persistence import HTMLService


class MockRedis(HTMLService):

    def __init__(self):
        self.redis = {}

    def get_html(self, key):
        return self.redis[key]

    def save_html(self, key, value):
        self.redis[key] = value

    def set_list_value(self, list_name, value, expire=None):
        if self.redis.get(list_name):
            self.redis.get(list_name).update({len(self.redis.get(list_name)): value})
        else:
            self.redis.update({list_name: {value}})

    def get_list(self, list_name, begin=0, end=-1):
        return self.redis[list_name]

    def set_expire(self, key, time):
        pass
