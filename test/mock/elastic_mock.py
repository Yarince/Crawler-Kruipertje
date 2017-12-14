from persistence import ParserService


class MockElastic(ParserService):

    def update_item(self, data_id, json, *args, **kwargs):
        self.parser = json

    def __init__(self):
        self.parser = {}
