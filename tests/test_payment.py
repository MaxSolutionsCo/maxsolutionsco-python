import datetime
from .commun import get_innov, response_keys, is_uuid, is_base64

get_innov()
import innov


class TestPayment(object):

    def test_payment_cash(self):
        data = {
            'CfdiType': 'P',
            'Currency': 'XXX',
            'Date': '2019-02-25 12:26:02',
            'ExpeditionPlace': '77500',
            'Folio': '20190002',
            'Issuer': {
                'FiscalRegime': '601',
                'Name': 'Max Solutions Co',
                'Rfc': 'LAN7008173R5'
            },
            'ItemPayments': [{
                'Currency': 'MXN',
                'OperationNumber': '872634',
                'PaymentDate': '2019-02-25 12:23:45',
                'PaymentForm': '01',
                'RelatedDocuments': [{
                    'AmountPaid': 50.0,
                    'BiasNumber': 1,
                    'Currency': 'MXN',
                    'Folio': '20190003',
                    'PaymentMethod': 'PPD',
                    'PreviousBalanceAmount': 116.0,
                    'Serie': 'IE',
                    'UnpaidBalanceAmount': 66.0,
                    'Uuid': '403EED2D-E9EF-4DE4-8AD6-72EE6DA90B4E'
                }],
                'Total': 50.0
            }],
            'Items': [{
                'Description': 'Pago',
                'ProductCode': '84111506',
                'Quantity': 1,
                'Subtotal': 0,
                'Total': 0,
                'UnitCode': 'ACT',
                'UnitPrice': 0
            }],
            'Receiver': {
                'CfdiUse': 'P01',
                'Name': 'Agrolait',
                'Rfc': 'XAXX010101000'
            },
            'Serie': 'B'
        }
        response = innov.CfdiPayment.stamp(data=data)
        response_keys(response)
        payload = response['Payload']
        assert isinstance(payload, dict)
        assert is_base64(payload['ContentXml'])
        assert is_uuid(payload['Uuid'])

    def test_payment_transfer(self):
        data = {
            'CfdiType': 'P',
            'Currency': 'XXX',
            'Date': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
            'ExpeditionPlace': '77500',
            'Folio': '20190003',
            'Issuer': {
                'FiscalRegime': '601',
                'Name': 'Max Solutions Co',
                'Rfc': 'LAN7008173R5'
            },
            'ItemPayments': [{
                'Currency': 'MXN',
                'IssuerBankAccount': '0195534960',
                'IssuerBankName': 'BBVA',
                'IssuerBankRfc': 'BBA830831LJ2',
                'OperationNumber': '283749827398',
                'PaymentDate': '2019-02-05 12:28:55',
                'PaymentForm': '03',
                'ReceiverBankAccount': '0195534989',
                'ReceiverBankName': 'BANORTE',
                'ReceiverBankRfc': 'BMN930209927',
                'RelatedDocuments': [{
                    'AmountPaid': 20.0,
                    'BiasNumber': 2,
                    'Currency': 'MXN',
                    'Folio': '20190003',
                    'PaymentMethod': 'PPD',
                    'PreviousBalanceAmount': 66.0,
                    'Serie': 'IE',
                    'UnpaidBalanceAmount': 46.0,
                    'Uuid': '403EED2D-E9EF-4DE4-8AD6-72EE6DA90B4E'
                }],
                'Total': 20.0
            }],
            'Items': [{
                'Description': 'Pago',
                'ProductCode': '84111506',
                'Quantity': 1,
                'Subtotal': 0,
                'Total': 0,
                'UnitCode': 'ACT',
                'UnitPrice': 0
            }],
            'Receiver': {
                'CfdiUse': 'P01',
                'Name': 'Agrolait',
                'Rfc': 'XAXX010101000'
            },
            'Serie': 'B'
        }
        response = innov.CfdiPayment.stamp(data=data)
        response_keys(response)
        payload = response['Payload']
        assert isinstance(payload, dict)
        assert is_base64(payload['ContentXml'])
        assert is_uuid(payload['Uuid'])
