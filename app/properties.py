from datetime import datetime


class Properties:
    REQUEST_HEADER = {'User-Agent': 'Kruipertje/1.0 (HAN Information Communication Academy, '
                                    'OOSE Groep 5, groep5ooseproject2017@gmail.com)'}
    SPIDER_MAX_DEPTH = 5
    SPIDER_MAX_PAGES = 10
    CRAWLER_MAX_THREADS = 1
    PARSER_MAX_THREADS = 1
    BLACKLIST_FILE = "blacklist.csv"
    REDIS_KEY_EXPIRE_TIME = 100
    MODULES_CONFIG_FILE = "modules.conf"
    CRAWLER_LOG_FILE = "crawler-" + str(datetime.now().strftime("%Y%m%d")) + ".log"
    SPIDER_LOG_FILE = "spider-" + str(datetime.now().strftime("%Y%m%d")) + ".log"
    # CRAWLER_LOG_FILE = "/var/log/crawler/crawler-" + str(datetime.now().strftime("%Y%m%d")) + ".log"
    # SPIDER_LOG_FILE = "/var/log/crawler/spider-" + str(datetime.now().strftime("%Y%m%d")) + ".log"

    class Elasticsearch:
        PARSER_INDEX = "parser"
        PARSER_DOC_TYPE = "data"


class RedisProperties:
    HOST = '94.23.202.32'
    PORT = 6379
    DB = 0
    PASSWORD = 'OOSEgroep%2017'


class ElasticsearchProperties:
    HOST = '94.23.202.32'
    PORT = 9200
