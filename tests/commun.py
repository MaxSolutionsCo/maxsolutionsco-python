# -*- coding: utf-8 -*-
# © Max Solutions, Co. All rights reserved.
import sys
import base64
import uuid
import io

sys.path.insert(0, 'innov')
import innov


def get_innov():
    return innov.configure({
        'mode': 'sandbox',  # sandbox or live
        'client_id': 'MchnpOAnR3tanm4DAdFJxyZkdiY5MHlKS.ymwfiyBTjgD.HUD_k5Pf6Lf1cT0Jci',
        'client_secret': 'Lswkus9FhETS7i-gJrUFFPv5lnFSJ-F3pB8ArK93dA74cLOvPfglZKJxIi9hl-44QbbqnsotLHSFk.F73gL-i3W0a5SqdivWXkUB76Yi9GaV6t7lNqsne2B6o4Mgl52b'
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
    file = io.open(path, "r", encoding='latin-1')
    content = file.read()
    if base64encode:
        return base64.b64encode(content.encode()).decode()
    return content
