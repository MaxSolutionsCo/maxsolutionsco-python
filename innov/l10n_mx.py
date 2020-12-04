# -*- coding: utf-8 -*-
# © Max Services, Biz. All rights reserved.
from .util import join_url
from .api import default as default_api


class L10MX:
    url = "/v1/mx/"
    
class MXCfdiv33(L10MX):

    @classmethod
    def Estado(cls, data, api=None):
        api = api or default_api()
        url = join_url(cls.url, '/cfdi-33/estado')
        return api.post(url, data)
    
    @classmethod
    def Cancelar(cls, data, api=None):
        api = api or default_api()
        url = join_url(cls.url, '/cfdi-33/cancelar')
        return api.post(url, data)

class MxPayroll(L10MX):

    @classmethod
    def Cfdiv33(cls, data, api=None):
        api = api or default_api()
        url = join_url(cls.url, '/cfdi-33/nomina-12')
        return api.post(url, data)
    
class MxForeignTrade(L10MX):

    @classmethod
    def Cfdiv33(cls, data, api=None):
        api = api or default_api()
        url = join_url(cls.url, '/cfdi-33/comercio-exterior-11')
        return api.post(url, data)
    