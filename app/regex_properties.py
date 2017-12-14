class RegexProperties:
    class LinkFinder:
        ABSOLUTE_URL = r'(https?:\/\/(www)?)?[-.a-zA-Z0-9]{2,256}\.nl\b([-a-zA-Z0-9%;/?:@&=$\-_.+!*\'(),]*)'
        RELATIVE_URL = r'((\.)+|(\/)+)*[-a-zA-Z0-9%;/?@&=$_.+!*\'(),]+\/?'

    class WordPress:
        THEME = r'\/wp-content\/themes\/([^\/]+)\/'
        VERSION = r'"WordPress ((\w+\.)+\w)"'

    class VATNumber:
        VAT_NUMBER = r'NL[0-9]{9}B[0-9]{2}'

    class Joomla:
        JOOMLA_SITE = r'(Joomla)! -[^\"]*'
        THEME = r'\/templates\/([^\/]*)'

    class PhoneNumber:
        # Check if there is no digit in front
        # Dutch country code or 0
        START = r'(?<![0-9-%])\(?(?:\+31|0031|0|31)'
        # 06 numbers
        MOBILE_NUMBER = r'(?:6\)?\.?-? ?[1-9][0-9]{7})'
        # company number
        COMPANY_NUMBER = r'(?:90[09]|800)\)?(?:[1-9][0-9]{6}|[1-9][0-9]{3})|(?:8[58][1-9][0-9]{7})'
        # Deprecated since 1.0
        #   NET_NUMBER = r'(?:(?:(?:[1-9]{2}\)?[0-9]?\)?[1-9][0-9]{5})|(?:[1-9][0-9][1-9][0-9]{6})))'
        # Check if there is no digit behind
        END = r'(?![0-9])'
