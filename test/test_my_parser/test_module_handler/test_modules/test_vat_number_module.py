import unittest

from my_parser.module_handler.my_modules.vat_number_module import VatNumberModule


class VATNumberModuleTest(unittest.TestCase):
    def setUp(self):
        self.sut = VatNumberModule()

    def test_handle_html_data_when_vat_number_found(self):
        self.sut.handle_html_data('<p>KvK 20091741 • btw&nbsp;NL140619562B01 • IBAN NL21 ABNA 0532 4840 10</p>')
        expected = {'vat_found': True, 'vat_numbers': ['NL140619562B01']}
        actual = self.sut.attributes
        self.assertDictEqual(expected, actual)

    def test_handle_html_data_when_multiple_vat_numbers_found(self):
        self.sut.handle_html_data('<p>KvK 20091741 • btw&nbsp;NL140619562B01 • NL142319562B02 • '
                                  'IBAN NL21 ABNA 0532 4840 10</p>')
        expected = {'vat_found': True, 'vat_numbers': ['NL142319562B02']}
        actual = self.sut.attributes
        self.assertDictEqual(expected, actual)

    def test_handle_html_data_when_duplicate_vat_numbers_found(self):
        self.sut.handle_html_data('<p>KvK 20091741 • btw&nbsp;NL140619562B01 • NL140619562B01 • NL140619562B01 •'
                                  'IBAN NL21 ABNA 0532 4840 10</p>')
        expected = {'vat_found': True, 'vat_numbers': ['NL140619562B01']}
        actual = self.sut.attributes
        self.assertDictEqual(expected, actual)

    def test_handle_html_data_when_not_vat_number_found(self):
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

        expected = {'vat_found': False}
        actual = self.sut.attributes
        self.assertDictEqual(expected, actual)

    def test_is_not_found(self):
        result = self.sut.is_found()
        self.assertFalse(result)

    def test_is_found(self):
        self.sut.attributes.update({'something': 'is now true'})
        result = self.sut.is_found()
        self.assertTrue(result)
