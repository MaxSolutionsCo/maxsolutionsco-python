<p align="center">  
  <a href="https://github.com/maxsbiz/sdk-python/actions?query=workflow%3APytest">
    <img src="https://github.com/maxsbiz/sdk-python/workflows/test/badge.svg">
  </a>
   <a href="LICENSE">  
    <img src="https://img.shields.io/github/license/maxsbiz/sdk-python?style=flat-square" />
  </a>
   <a href="semv.toml">
    <img src="https://img.shields.io/badge/semv-1.0.9-green">
  </a>
</p>
# Max Services Biz Python SDK

## Contenido
* Instación
* Configuracion
    * Global
    * Variables de entorno
    * No global
* Contabilidad y Finanzas 
    * Certificados
        * Subir CSD
        * Actualizar CSD
    * Facturacion
        * Timbrar CFDI 3.3
        * Cancelar CFDI 3.3
    * Herramientas
        * Crear cadena TFD y CFDI
        * Validar UUID SAT
* Licencia
* Autor

## Instalación 

Usando ``pip``: 

```bash
    pip install git+https://github.com/maxsbiz/sdk-python
```
o: 
```bash
    git clone https://github.com/maxsbiz/sdk-python.git
    cd sdk-python
    python setup.py install
```

## Configuración 
Regístrese para obtener una cuenta y obtenga su ``client_id`` y ``client_secret`` en [Producción](https://api.maxs.biz) o [Pruebas](https://api.sandbox.maxs.biz).
```python 
import innov 
innov.configure({
    'mode':'sandbox', # sandbox or live
    'client_id':'MchnpOAnR3tanm4DAdFJxyZkdiY5MHlKS.ymwfiyBTjgD.HUD_k5Pf6Lf1cT0Jci',
    'client_secret':'Lswkus9FhETS7i-gJrUFFPv5lnFSJ-F3pB8ArK93dA74cLOvPfglZKJxIi9hl-44QbbqnsotLHSFk.F73gL-i3W0a5SqdivWXkUB76Yi9GaV6t7lNqsne2B6o4Mgl52b'
})
```
configurar a través de variables de entorno

```bash
export INNOV_MODE=sandbox   
export INNOV_CLIENT_ID=MchnpOAnR3tanm4DAdFJxyZkdiY5MHlKS.ymwfiyBTjgD.HUD_k5Pf6Lf1cT0Jci
export INNOV_CLIENT_SECRET=Lswkus9FhETS7i-gJrUFFPv5lnFSJ-F3pB8ArK93dA74cLOvPfglZKJxIi9hl-44QbbqnsotLHSFk.F73gL-i3W0a5SqdivWXkUB76Yi9GaV6t7lNqsne2B6o4Mgl52b
```
Configurar a través de un objeto API no global
```python
api = innov.Api({
    'mode':'sandbox',
    'client_id':'MchnpOAnR3tanm4DAdFJxyZkdiY5MHlKS.ymwfiyBTjgD.HUD_k5Pf6Lf1cT0Jci',
    'client_secret':'Lswkus9FhETS7i-gJrUFFPv5lnFSJ-F3pB8ArK93dA74cLOvPfglZKJxIi9hl-44QbbqnsotLHSFk.F73gL-i3W0a5SqdivWXkUB76Yi9GaV6t7lNqsne2B6o4Mgl52b'
})
    
```
## Contabilidad y finanzas
### Certificados
#### Subir CSD
```python
data = {
    'CompanyName': "Max Solutions, Co",
    'Rfc': "LAN7008173R5",
    'Certificate': "aG9s...YQo=",
    'PrivateKey': "aG9s...YQo=",
    'PrivateKeyPassword': "12345678a",
}
response = innov.CfdiCsd.create(data=data)

```
#### Actualizar CSD
```python
data = {
    'CompanyName': "Max Solutions, Co",
    'Rfc': "LAN7008173R5",
    'Certificate': "aG9s...YQo=",
    'PrivateKey': "aG9s...YQo=",
    'PrivateKeyPassword': "12345678a",
}
response = innov.CfdiCsd.update(data=data)

```
### Facturación 
#### Timbrar CFDI 3.3 
```python
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
```
#### Cancelar CFDI 3.3 
```python
response = innov.Cfdi.cancel(rfc_issuer='LAN7008173R5', uuid='E4CF456D-C482-4F10-A9B5-F5A0CE4AB0FB')
```
### Herramientas
####  Crear cadena TFD y CFDI
```python
data = {
    'ContentXml': "aG9s...YQo="
}
response = innov.Cfdi.chain(data=data)
# or 
response = innov.Cfdi.chain_tfd(data=data)
# or 
response = innov.Cfdi.chain_cfdi(data=data)

```
#### Validar UUID SAT
```python

data = {
    "Uuid": "E4CF456D-C482-4F10-A9B5-F5A0CE4AB0FB",
    "Issuer": "LAN7008173R5",
    "Receiver": "XAXX010101000",
    "Amount": 255.20
}
response = innov.Cfdi.validate_uuid(data=[data])

```
