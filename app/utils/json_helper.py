import json


class JsonHelper:
    """
    This class can help with JSON strings
    """
    @staticmethod
    def to_json(value):
        """
        This method changes a dict to json value
        :param value: anything
        :return: json string
        """
        return json.dumps(value, ensure_ascii=False)

    @staticmethod
    def to_dict(value):
        """
        This method takes a json string and returns a dict
        :param value: json string
        :return: dict
        """
        return json.loads(value)
