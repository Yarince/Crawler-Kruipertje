from properties import Properties
from datetime import datetime
from utils import HashService, DomainParser, CfgReader, ClassReturner, JsonHelper


class DataParser:

    def __init__(self, url, redis, name, parser_service):
        self.url = url
        self.redis = redis
        self.name = name
        self.parser_service = parser_service

    def parse(self):
        """
        Loops through all my_modules in the Module enum. This is the main method of the DataParser class
        :return: Nothing
        """
        print(self.name, "is now parsing: {0}".format(self.url))
        modules_info = self.__loop_through_modules()
        if len(modules_info) > 0:
            time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
            modules_info.update({"url": self.url.url_string})
            modules_info.update({"@timestamp": time + "Z"})
            self.__save_to_database(JsonHelper.to_json(modules_info))
        else:
            print(self.name, "found nothing.")

    def __get_items_from_redis_list(self):
        """
        Returns a list with html code from a url.
        :return: List
        """
        redis_key = HashService.num_md5(DomainParser.get_domain_name(self.url.url_string))
        return self.redis.get_list(redis_key, 0, -1)

    def __loop_through_modules(self):
        """
        Method for looping through all the my_modules. This method will return a dict with all results.
        :return: Dict
        """
        result = dict()
        for mod in self.__get_available_modules():
            module_instance = mod()
            self.__loop_through_pages(module_instance)
            if len(module_instance.attributes) > 0:
                result.update(module_instance.attributes)
        return result

    def __loop_through_pages(self, mod_instance):
        """
        Loops trough all pages for a given module. Exits early if the module has been found.
        :param mod_instance:instance of a module
        :return: Boolean
        """
        for page in self.__get_items_from_redis_list():
            mod_instance.handle_html_data(str(page))
            if not mod_instance.run_all_pages and mod_instance.is_found():
                return True

    @staticmethod
    def __get_available_modules():
        """
        This method will return all modules that have been activated
        :return: Set()
        """
        conf = CfgReader(Properties.MODULES_CONFIG_FILE)
        result = set()
        for var in conf.get_section('my.modules'):
            try:
                file, item = var.split('.')
                kls = ClassReturner.get_class('my_parser.module_handler.my_modules.{0}'.format(file), item)
                if kls is not None:
                    result.add(kls)
            except ValueError as e:
                print("Cfg Error on {0}: {1}".format(var, e.args))
        return result

    def __save_to_database(self, json):
        """
        This method will save the json string to the selected database.
        this method uses the id as key.
        :param json: the json to be stored in the database
        :return: Nothing
        """
        id = HashService.num_md5(self.url.url_string)
        print(self.name, "found: {0}".format(json))
        self.parser_service.update_item(id, json)
