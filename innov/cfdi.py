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
    def cancel(cls, rfc, uuid, api=None):
        api = api or default_api()
        path = join_url(cls.path, 'stamp', rfc, uuid)
        return api.delete(path)

    @classmethod
    def validate_uuid(cls, data, api=None):
        """

        :param data:
        :param api:
        :return:
        """
        path = join_url(cls.path, 'validate/uuid')
        api = api or default_api()
        return api.post(path, data)
