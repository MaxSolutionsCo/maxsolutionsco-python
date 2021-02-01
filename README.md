<p align="center">  
  <a href="https://github.com/maxsbiz/sdk-python/actions?query=workflow%3APytest">
    <img src="https://github.com/maxsbiz/sdk-python/workflows/test/badge.svg">
  </a>
   <a href="LICENSE">  
    <img src="https://img.shields.io/github/license/maxsbiz/sdk-python?style=flat-square" />
  </a>
   <a href="semv.toml">
    <img src="https://img.shields.io/badge/semv-1.0.13-green">
  </a>
</p>

# SDK Python

## Instalación

Usando ``pip``:

```bash
    pip install git+https://github.com/maxservicesbiz/sdk-python
```

o: 

```bash
    git clone https://github.com/maxservicesbiz/sdk-python.git
    cd sdk-python
    python setup.py install
```

## Configuración

Regístrese para obtener una cuenta y obtenga su ``client_id`` y ``client_secret`` en https://maxs.biz.

```python
import innov 
innov.configure({
    'mode':'sandbox', # sandbox or live
    'client_id':'jFBEDC97BOrxUIPuO4mB9oGhCF1MwK7f',
    'client_secret':'SoEh6njLpSlTyrLcoyjbW4IzLfod74G3uA2YmL1Tt.hqrwhcnCGK.BDZ_F91N9FiiKWaBVSpyhH2gvOB.W8LB0E2qgd31XvT'
})
```

configurar a través de variables de entorno

```bash
export INNOV_MODE=sandbox   
export INNOV_CLIENT_ID=jFBEDC97BOrxUIPuO4mB9oGhCF1MwK7f
export INNOV_CLIENT_SECRET=SoEh6njLpSlTyrLcoyjbW4IzLfod74G3uA2YmL1Tt.hqrwhcnCGK.BDZ_F91N9FiiKWaBVSpyhH2gvOB.W8LB0E2qgd31XvT
```

Configurar a través de un objeto API no global

```python
api = innov.Api({
    'mode':'sandbox',
    'client_id':'jFBEDC97BOrxUIPuO4mB9oGhCF1MwK7f',
    'client_secret':'SoEh6njLpSlTyrLcoyjbW4IzLfod74G3uA2YmL1Tt.hqrwhcnCGK.BDZ_F91N9FiiKWaBVSpyhH2gvOB.W8LB0E2qgd31XvT'
})
    
```
