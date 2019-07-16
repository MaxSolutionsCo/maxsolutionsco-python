# -*- coding: utf-8 -*-
# © Max Solutions, Co. All rights reserved.
import random
import datetime
from .commun import is_base64, response_keys, is_uuid, open_file, get_innov
get_innov()
import innov


class TestCfdi(object):

    def test_validate_uuid(self):
        data = {
            "Uuid": "E4CF456D-C482-4F10-A9B5-F5A0CE4AB0FB",
            "Issuer": "LAN7008173R5",
            "Receiver": "XAXX010101000",
            "Amount": 255.20
        }
        response = innov.Cfdi.validate_uuid(data=[data, data])
        response_keys(response)
        payload = response['Payload']
        assert isinstance(payload, list)
        for item in payload:
            for key in ['Status', 'Receiver', 'Issuer', 'IsCancelable', 'StatusCode', 'CancellationStatus', 'Amount',
                        'Uuid']:
                assert key in list(item.keys())

    def test_stamp(self):
        data = {
            "Folio": str(random.randint(1, 1000000)),
            "Serie": "R",
            "Currency": "MXN",
            "Rate": 1,
            "Date": datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
            "ExpeditionPlace": "77500",
            "PaymentConditions": "CREDITO A SIETE DIAS",
            "CfdiType": "I",
            "PaymentForm": "03",
            "PaymentMethod": "PUE",
            "Receiver": {
                "Rfc": "XAXX010101000",
                "Name": "RADIAL SOFTWARE SOLUTIONS",
                "CfdiUse": "G02"
            },
            "Issuer": {
                "FiscalRegime": "601",
                "Name": "MAx Solutions Co",
                "Rfc": "LAN7008173R5"
            },
            "Items": [
                {
                    "ProductCode": "10101504",
                    "IdentificationNumber": "EDL",
                    "Description": "Tarjeta gráfica",
                    "Unit": "Unidad(es)",
                    "UnitCode": "A14",
                    "UnitPrice": 50,
                    "Quantity": 2,
                    "Subtotal": 100,
                    "Taxes": [
                        {
                            "Total": 16,
                            "Name": "IVA",
                            "Code": "002",
                            "Type": "Tasa",
                            "Base": 100,
                            "Rate": 0.16,
                            "IsRetention": False
                        }
                    ],
                    "Total": 116
                }
            ]
        }
        response = innov.Cfdi.stamp(data=data)
        response_keys(response)
        payload = response['Payload']
        assert isinstance(payload, dict)
        assert is_base64(payload['ContentXml'])
        assert is_uuid(payload['Uuid'])

    """
    def test_stamp_cancel(self):
        
            Staging environment is not possible cancel UUID,
            only allowed on live environment.
        
        
        response = innov.Cfdi.cancel('LAN7008173R5', 'E4CF456D-C482-4F10-A9B5-F5A0CE4AB0FB')
        assert response_keys(response)
        payload = response['Payload']
        assert isinstance(payload, dict)
        assert 'State' in list(payload.keys())
    """

    def test_chain(self):
        data = {
            'ContentXml': open_file('tests/provision/E4CF456D-C482-4F10-A9B5-F5A0CE4AB0FB.xml', base64encode=True)
        }
        response = innov.Cfdi.chain(data)
        response_keys(response)
        payload = response['Payload']
        assert isinstance(payload, dict)
        assert 'ChainTfd' in list(payload.keys())
        assert 'ChainCfdi' in list(payload.keys())

    def test_chain_tfd(self):
        data = {
            'ContentXml': open_file('tests/provision/E4CF456D-C482-4F10-A9B5-F5A0CE4AB0FB.xml', base64encode=True)
        }
        response = innov.Cfdi.chain_tfd(data)
        response_keys(response)
        payload = response['Payload']
        assert isinstance(payload, dict)
        assert 'ChainTfd' in list(payload.keys())

    def test_chain_cfdi(self):
        data = {
            'ContentXml': open_file('tests/provision/E4CF456D-C482-4F10-A9B5-F5A0CE4AB0FB.xml', base64encode=True)
        }
        response = innov.Cfdi.chain_cfdi(data)
        response_keys(response)
        payload = response['Payload']
        assert isinstance(payload, dict)
        assert 'ChainCfdi' in list(payload.keys())
