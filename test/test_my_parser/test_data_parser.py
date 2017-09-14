import unittest
from domain import Url
from app.my_parser import DataParser
from properties import Properties
from test.mock import MockRedis, MockElastic
from utils import HashService, DomainParser


class DataParserTest(unittest.TestCase):

    def setUp(self):
        self.url = Url("http://example.com", 1)
        name = "name"
        Properties.MODULES_CONFIG_FILE = '../app/modules.conf'
        self.redis = MockRedis()
        self.elastic = MockElastic()
        self.sut = DataParser(self.url, self.redis, name, self.elastic)

    def test_get_items_from_redis_list(self):
        expected = '{"joomla": true, "joomla_theme": "joomla", "url": "http://example.com"}'
        key = HashService.num_md5(DomainParser.get_domain_name(self.url.url_string))
        self.redis.set_list_value(key,
                                  '<meta name="description" content="Joomla! is the mobile-ready and user-friendly way '
                                  'to build your website. Choose from thousands of features and designs. Joomla! '
                                  'is free and open source." /><meta name="generator" content="Joomla! - Open Source '
                                  'Content Management" /><title>Joomla! The CMS Trusted By Millions for their Websites'
                                  '</title><link href="/templates/joomla/images/apple-touch-icon-180x180.png" '
                                  'rel="apple-touch-icon" sizes="180x180" />')
        self.sut.parse()
        self.assertEqual(expected, self.elastic.parser)
        pass

    def test_parser_found_nothing(self):
        key = HashService.num_md5(DomainParser.get_domain_name(self.url.url_string))
        self.redis.set_list_value(key,
                                  '<!DOCTYPE html> <html><head><meta charset = "utf-8"> '
                                  '<title>PLEX-Server</title> </head> <body> '
                                  '<h1><font color="#FF0000" size="+5" style="text-align: center">'
                                  '<marquee behavior="alternate" bgcolor="yellow" scrollamount="10">'
                                  'Welkom</marquee><br><br><br> <a href="/transmission/web/" '
                                  'onclick="javascript:event.target.port=9091">TORRENTS</a> <br> '
                                  '<a href="http://app.plex.tv/web/app#">PLEX</a> <br>'
                                  ' <a href="../htmlshit">Onzin</a> <br> <a href="../oops.html">Oops</a>'
                                  ' <br> <a href="../bp-webdev">webshop</a>'
                                  ' <br> <a href="../EenmaalAndermaal">EenmaalAndermaal</a>'
                                  ' <br> <a href="../EenmaalAndermaal-static">EenmaalAndermaal - static</a> </font>'
                                  ' </h1> </body></html>')
        self.sut.parse()
        self.assertEqual({}, self.elastic.parser)
        print(self.elastic.parser)
