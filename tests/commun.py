import base64
import uuid


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
    file = open(path, "r")
    content = file.read()
    if base64encode:
        return base64.b64encode(content.encode()).decode()
    return content
