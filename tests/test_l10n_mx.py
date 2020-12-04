from .commun import get_innov, is_base64, is_uuid
from datetime import datetime
import json
import random

get_innov()
import innov

sat_datetime = lambda: datetime.today().strftime('%Y-%m-%d %H:%M')
sat_folio = lambda: str(random.randint(1, 1000000000000000000000))

def test_payroll_cfdiv33():
    with open('tests/l10n_mx/payrollv12.json') as f:
        data = json.load(f)
        data['Fecha'] = sat_datetime()
        data["Folio"] = sat_folio()
        response = innov.MxPayroll.Cfdiv33(data)
        assert response.get('Success')
        assert is_base64(response.get('Payload').get('Document'))
        assert is_uuid(response.get('Payload').get('Uuid'))

def test_foreigntrade_cfdiv33():
    with open('tests/l10n_mx/foreigntradev11.json') as f:
        data = json.load(f)
        data['Fecha'] = sat_datetime()
        data["Folio"] = sat_folio()
        response = innov.MxForeignTrade.Cfdiv33(data)
        assert response.get('Success')
        assert is_base64(response.get('Payload').get('Document'))
        assert is_uuid(response.get('Payload').get('Uuid'))
        
def test_cfdiv33_estado():
    with open('tests/l10n_mx/cfdiv33Statev2.json') as f:
        data = json.load(f)
        response = innov.MXCfdiv33.Estado(data)
        assert response.get('Success')

# TODO: Sandbox is not working
#def test_cfdiv33_cancelar():
#    with open('tests/l10n_mx/cfdiv33_cancel.json') as f:
#        data = json.load(f)
#        response = innov.MXCfdiv33.Cancelar(data)
#        assert response.get('Success')