import sys

sys.path.insert(0, 'innov')
import innov

api = innov.configure({
    'mode': 'sandbox',  # sandbox or live
    'client_id': 'MchnpOAnR3tanm4DAdFJxyZkdiY5MHlKS.ymwfiyBTjgD.HUD_k5Pf6Lf1cT0Jci',
    'client_secret': 'Lswkus9FhETS7i-gJrUFFPv5lnFSJ-F3pB8ArK93dA74cLOvPfglZKJxIi9hl-44QbbqnsotLHSFk.F73gL-i3W0a5SqdivWXkUB76Yi9GaV6t7lNqsne2B6o4Mgl52b'
})


class TestCfdi(object):

    def test_sign_in(self):
        assert len(api.get_token_hash()) == 498, "Fail authentication"

    def test_validate_uuid(self):
        data = {
            "Uuid": "E4CF456D-C482-4F10-A9B5-F5A0CE4AB0FB",
            "Issuer": "XAXX010101000",
            "Receiver": "XAXX010101000",
            "Amount": 255.20
        }
        response = innov.Cfdi.validate_uuid(data=[data, data])
        for key in ['Message', 'Payload', 'Success']:
            assert key in list(response.keys())
        payload = response['Payload']
        assert isinstance(payload, list)
        for item in payload:
            for key in ['Status', 'Receiver', 'Issuer', 'IsCancelable', 'StatusCode', 'CancellationStatus', 'Amount',
                    'Uuid']:
                assert key in list(item.keys())
