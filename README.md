# Max Solutions Co Python SDK

## Installation 
Install usign pip : 

```bash
    pip install git+https://github.com/MaxSolutionsCo/innov-python
```
or : 
```bash
    git clone https://github.com/MaxSolutionsCo/innov-python.git
    cd innov-python
    python setup.py install
```

## Configuration 
Register for an account and get your client_id and client_secret at [Live](https://max-solutions.co) or [Sandbox](https://api.sandbox.max-solutions.co).
```python 
import innov 
innov.configure({
    'mode':'sandbox', # sandbox or live
    'client_id':'MchnpOAnR3tanm4DAdFJxyZkdiY5MHlKS.ymwfiyBTjgD.HUD_k5Pf6Lf1cT0Jci',
    'client_secret':'Lswkus9FhETS7i-gJrUFFPv5lnFSJ-F3pB8ArK93dA74cLOvPfglZKJxIi9hl-44QbbqnsotLHSFk.F73gL-i3W0a5SqdivWXkUB76Yi9GaV6t7lNqsne2B6o4Mgl52b'
})
```

configure through environment variables 

```bash
export INNOV_MODE=sandbox   
export INNOV_CLIENT_ID=MchnpOAnR3tanm4DAdFJxyZkdiY5MHlKS.ymwfiyBTjgD.HUD_k5Pf6Lf1cT0Jci
export INNOV_CLIENT_SECRET=Lswkus9FhETS7i-gJrUFFPv5lnFSJ-F3pB8ArK93dA74cLOvPfglZKJxIi9hl-44QbbqnsotLHSFk.F73gL-i3W0a5SqdivWXkUB76Yi9GaV6t7lNqsne2B6o4Mgl52b
```
Configure through no-global API object 
```bash
api = innov.Api({
    'mode':'sandbox',
    'client_id':'MchnpOAnR3tanm4DAdFJxyZkdiY5MHlKS.ymwfiyBTjgD.HUD_k5Pf6Lf1cT0Jci',
    'client_secret':'Lswkus9FhETS7i-gJrUFFPv5lnFSJ-F3pB8ArK93dA74cLOvPfglZKJxIi9hl-44QbbqnsotLHSFk.F73gL-i3W0a5SqdivWXkUB76Yi9GaV6t7lNqsne2B6o4Mgl52b'
})
    
```


## License
* [Apache 2.0](LICENSE)
## Authors 
* [Max Solutions, Co](https://max-solutions.co)
