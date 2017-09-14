import sys

from crawler.crawler import Crawler
from enums import DB, HTML, PARSER
from my_exceptions import BlacklistNotFoundError
from my_parser import Parser


def main():
    parser = Parser(HTML.REDIS, PARSER.ELASTICSEARCH)
    """Crawler start"""
    crawler = Crawler(DB.MYSQL, HTML.REDIS, parser)

    try:
        crawler.start()
    except KeyboardInterrupt:
        crawler.stop()
        sys.exit(0)

if __name__ == '__main__':
    main()
