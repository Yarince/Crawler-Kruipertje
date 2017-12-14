import unittest

from app.my_parser.module_handler.my_modules.joomla_module import JoomlaModule


class JoomlaModuleTest(unittest.TestCase):
    def setUp(self):
        self.sut = JoomlaModule()

    def test_handle_html_data_when_joomla_site(self):
        self.sut.handle_html_data('<meta name="description" content="Joomla! is the mobile-ready and user-friendly way '
                                  'to build your website. Choose from thousands of features and designs. Joomla! '
                                  'is free and open source." /><meta name="generator" content="Joomla! - Open Source '
                                  'Content Management" /><title>Joomla! The CMS Trusted By Millions for their Websites'
                                  '</title><link href="/templates/joomla/images/apple-touch-icon-180x180.png" '
                                  'rel="apple-touch-icon" sizes="180x180" />')
        expected = {'joomla_found': True, 'joomla_theme': 'joomla'}
        actual = self.sut.attributes
        self.assertDictEqual(expected, actual)

    def test_handle_html_data_when_not_joomla_site(self):
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
        expected = {'joomla_found': False}
        actual = self.sut.attributes
        self.assertDictEqual(expected, actual)

    def test_is_not_found(self):
        result = self.sut.is_found()
        self.assertFalse(result)

    def test_is_found(self):
        self.sut.attributes.update({'something': 'is now true'})
        result = self.sut.is_found()
        self.assertTrue(result)
