import unittest

from app.my_parser.module_handler.my_modules.wordpress_module import WordPressModule

"""
    Import Error
"""


class WordPressModuleTest(unittest.TestCase):
    def setUp(self):
        self.sut = WordPressModule()

    def test_error(self):
        # TODO: Custom exception maken
        with self.assertRaises(Exception):
            self.sut.error("testError")

    def test_handle_html_data_when_wordpress_site(self):
        self.sut.handle_html_data('<link rel="shortcut icon" type="image/x-icon" '
                                  'href="http://demo.qodeinteractive.com/bridge/'
                                  'wp-content/themes/bridge/img/favicon.ico"> '
                                  '<meta name="generator" content="WordPress 4.7.5" />')
        expected = {'wordpress': True, 'wordpress_theme': 'bridge', 'wordpress_version': '4.7.5'}
        actual = self.sut.attributes
        self.assertDictEqual(expected, actual)

    def test_handle_html_data_when_not_wordpress_site(self):
        self.sut.handle_html_data('<!DOCTYPE html> <html><head><meta charset = "utf-8"> '
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
        expected = {}
        actual = self.sut.attributes
        self.assertDictEqual(expected, actual)

    def test_is_not_found(self):
        result = self.sut.is_found()
        self.assertFalse(result)

    def test_is_found(self):
        self.sut.attributes.update({'something': 'is now true'})
        result = self.sut.is_found()
        self.assertTrue(result)
