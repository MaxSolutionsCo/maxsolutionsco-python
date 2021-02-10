# -*- coding: utf-8 -*-
# © Yonn, Xyz. All rights reserved.
from .util import join_url
from .api import default as default_api


class Cfdi:
    path = 'v1/cfdi/'

    @classmethod
    def stamp(cls, data, api=None):
        api = api or default_api()
        path = join_url(cls.path, 'stamp')
        return api.post(path, data)

    @classmethod
    def cancel(cls, rfc_issuer, uuid, api=None):
        api = api or default_api()
        path = join_url(cls.path, 'stamp', rfc_issuer, uuid)
        return api.delete(path)

    @classmethod
    def validate_uuid(cls, data, api=None):
        path = join_url(cls.path, 'validate','uuid')
        api = api or default_api()
        return api.post(path, data)

    @classmethod
    def chain(cls, data, api=None):
        path = join_url(cls.path, 'chain')
        api = api or default_api()
        return api.post(path, data)

    @classmethod
    def chain_cfdi(cls, data, api=None):
        path = join_url(cls.path, 'chain','cfdi')
        api = api or default_api()
        return api.post(path, data)

    @classmethod
    def chain_tfd(cls, data, api=None):
        path = join_url(cls.path, 'chain','tfd')
        api = api or default_api()
        return api.post(path, data)

    @classmethod
    def status(cls, rfc_issuer, uuid, api=None):
        api = api or default_api()
        path = join_url(cls.path, 'stamp','status', rfc_issuer, uuid)
        return api.get(path)


class CfdiPayment:
    path = 'v1/cfdi/payment/'

    @classmethod
    def stamp(cls, data, api=None):
        api = api or default_api()
        path = join_url(cls.path, 'stamp')
        return api.post(path, data)


class CfdiCsd:
    path = 'v1/cfdi/'

    @classmethod
    def create(cls, data, api=None):
        api = api or default_api()
        path = join_url(cls.path, 'csd')
        return api.post(path, data)

    @classmethod
    def update(cls, data, api=None):
        api = api or default_api()
        path = join_url(cls.path, 'csd', data.get('Rfc'))
        return api.put(path, data)