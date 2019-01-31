# -*- coding: utf-8 -*-
# © Yonn, Xyz. All rights reserved.
from .util import join_url
from .api import default as default_api


class Message:
    path = 'v1/message/'

    @classmethod
    def sms(cls, data, api=None):
        api = api or default_api()
        path = join_url(cls.path, 'sms')
        return api.post(path, data)