# Innov Python SDK

## Instaltion 
install usign pip : 

```bash
    pip install https://github.com/YonnXyz/innov-python
```
## Configuration 
Register for an account and get your client_id and secret at [Innov Portal](https://innov.biz).
```python 
import innov 
innov.configure({
    'mode':'sandbox',
    'client_id':'sandbox@innov.biz',
    'client_secret':'p4$$w0rd'
})
```

configure through environment variables 

```bash
export INNOV_MODE=sandbox   # sandbox or live
export INNOV_CLIENT_ID=sandbox@innov.biz
export INNOV_CLIENT_SECRET=p4$$word    
```
Configure through no-global API object 
```bash
api = innov.Api({
    'mode':'sandbox',
    'client_id':'sandbox@innov.biz',
    'client_secret':'p4$$w0rd'
})
    
```


## License
* [Apache 2.0](LICENSE)
## Authors 
* [Yonn, Xyz](https://yonn.xyz)
