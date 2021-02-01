# -*- coding: utf-8 -*-
# © Max Solutions, Co. All rights reserved.
import pdb
import sys
import base64
import uuid
import platform

sys.path.insert(0, 'innov')
import innov


def get_innov():
    return innov.configure({
        'mode': 'sandbox',  # sandbox or live
        'client_id': 'jFBEDC97BOrxUIPuO4mB9oGhCF1MwK7f',
        'client_secret': 'SoEh6njLpSlTyrLcoyjbW4IzLfod74G3uA2YmL1Tt.hqrwhcnCGK.BDZ_F91N9FiiKWaBVSpyhH2gvOB.W8LB0E2qgd31XvT'
    })


def is_base64(s):
    try:
        s = s.encode()
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False


def is_uuid(s):
    s = str(s).lower()
    try:

        uuid_obj = uuid.UUID(s, version=4)
    except Exception:
        return False
    return str(uuid_obj) == s


def response_keys(response):
    for key in ['Message', 'Payload', 'Success']:
        assert key in list(response.keys())


def open_file(path, base64encode=False):
    content = ""
    if platform.python_version()[:3] == '2.7':
        _file = open(path, "r")
        content = str(_file.read())
    if float(platform.python_version()[:3]) >= 3.0:
        _file = open(path, "r",encoding='latin-1')
        content = _file.read().encode()
    if base64encode:
        return base64.b64encode(content).decode()
    return content

