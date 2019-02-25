# -*- coding: utf-8 -*-
# © Max Solutions, Co. All rights reserved.
from .commun import get_innov, open_file, response_keys
import random

get_innov()
import innov

rfc = "TEST%s" % (random.randint(100000000, 999999999))


class TestCsd:
    def test_create(self):
        data = {
            'CompanyName': "Max Solutions, Co",
            'Rfc': rfc,
            'Certificate': open_file("tests/provision/LAN7008173R5.cer", base64encode=True),
            'PrivateKey': open_file("tests/provision/LAN7008173R5.key", base64encode=True),
            'PrivateKeyPassword': "12345678a",
        }
        response = innov.CfdiCsd.create(data=data)
        response_keys(response)

    def test_update(self):
        data = {
            'CompanyName': "Max Solutions, Co - %s" % rfc,
            'Rfc': rfc,
            'Certificate': open_file("tests/provision/LAN7008173R5.cer", base64encode=True),
            'PrivateKey': open_file("tests/provision/LAN7008173R5.key", base64encode=True),
            'PrivateKeyPassword': "12345678a",
        }
        response = innov.CfdiCsd.update(data=data)
        response_keys(response)
