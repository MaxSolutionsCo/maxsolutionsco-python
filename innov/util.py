# -*- coding: utf-8 -*-
# © Yonn, Xyz. All rights reserved.
import re
import base64
import platform
import logging

log = logging.getLogger(__name__)

if platform.python_version()[0] == "3":
    text_type = str
else:
    text_type = unicode


def merge_dict(data, *override):
    """
    Merges any number of dictionaries together, and returns a single dictionary
    Usage::
        >>> util.merge_dict({'new': 'add'}, {1: 2}, {'innov': 'biz'})
        {1: 2, 'new': 'add', 'innov': 'biz'}
    """
    result = {}
    for current_dict in (data,) + override:
        result.update(current_dict)
    return result


def join_url(url, *paths):
    """
    Joins individual URL strings together, and returns a single string.
    Usage::
        >>> util.join_url('api.sandbox.innov.biz', '/v1','/cfdi/')
        'api.sandbox.innov.biz/v1/demo/'
    """
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url


def base64url_decode(input):
    if isinstance(input, text_type):
        input = input.encode('ascii')
    rem = len(input) % 4
    if rem > 0:
        input += b'=' * (4 - rem)
    decode = base64.urlsafe_b64decode(input)
    if isinstance(decode, bytes):
        decode = decode.decode('utf-8')
    return decode


def error_tracking(**kwargs):
    # log = kwargs.get('log', log)
    # name = kwargs.get('name',__name__)

    """if kwargs.get('info'):
        log.info(kwargs.get('info'))
    elif kwargs.get('debug'):
        log.debug(kwargs.get('debug'))
    elif kwargs.get('error'):
        log.error(kwargs.get('error'))
    """
    for index in kwargs:
        if index not in ['log', 'name']:
            print(kwargs.get(index) + "\n")
