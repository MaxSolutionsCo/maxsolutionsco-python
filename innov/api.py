# -*- coding: utf-8 -*-
# © Yonn, Xyz. All rights reserved.
import requests
import datetime
import base64
import logging
import os
import platform
from .config import __endpoint_map__, __version__
from .util import join_url, merge_dict, base64url_decode, error_tracking
from .exceptions import *

log = logging.getLogger(__name__)


class Api(object):
    user_agent = "Innov-Python-SDK %s (Requests: %s, Python: %s)" % (
        __version__, requests.__version__, platform.python_version())

    def __init__(self, options=None, **kwargs):
        kwargs = options or kwargs

        self.mode = kwargs.get('mode', 'sandbox')
        if self.mode not in __endpoint_map__.keys():
            raise InvalidConfig('Configuration mode invalid', 'Received: {}'.format(self.mode),
                                'Required: {}'.format(__endpoint_map__.keys()))
        self.endpoint = self.get_default_endpoint()
        # Mandatory parameter, so no using "dict.get"
        self.client_id = kwargs['client_id']
        self.client_secret = kwargs['client_secret']
        self.token_hash = None
        self.token_request_at = None
        self.options = kwargs

    def get_default_endpoint(self):
        return __endpoint_map__.get(self.mode)

    def basic_auth(self):
        """Find basic auth, and returns base64 encoded
        """
        credentials = "%s:%s" % (self.client_id, self.client_secret)
        return base64.b64encode(credentials.encode('utf-8')).decode('utf-8').replace("\n", "")

    def get_token_hash(self, authorization_code=None, refresh_token=None, headers=None):
        """Generate new token by making a POST request
        """
        path = "/v1/signin"
        payload = {
            "Username": self.client_id,
            "Password": self.client_secret
        }
        method = "POST"
        if authorization_code is not None:
            """payload = "grant_type=authorization_code&response_type=token&redire" \
                      "ct_uri=urn:ietf:wg:oauth:2.0:oob&code=" + \
                      authorization_code
            """
            pass
        elif refresh_token is not None:
            path = "/v1/token-refresh"
            headers = merge_dict(headers, {'Authorization': 'Bearer %s' % refresh_token})
            method = "PUT"
        else:
            self.validate_token_hash()
            if self.token_hash is not None:
                # return cached copy
                return self.token_hash

        token = self.http_call(
            join_url(self.endpoint, path), method,
            json=payload,
            headers=merge_dict({
                "Authorization": "Basic %s" % self.basic_auth(),
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": self.user_agent
            }, headers or {}))
        token = token.get('Payload').get('Token')
        if refresh_token is None and authorization_code is None:
            # cache token for re-use in normal case
            self.token_request_at = datetime.datetime.now()
            self.token_hash = token
        return token

    def validate_token_hash(self):
        """Checks if token duration has expired and if so resets token
        """
        if self.token_request_at and self.token_hash:
            token_hash_exp = self.token_hash.split('.')[1]
            toke_hash_decode = json.loads(base64url_decode(token_hash_exp))
            if datetime.datetime.now() > datetime.datetime.fromtimestamp(toke_hash_decode.get("exp")):
                self.token_hash = None

    def get_access_token(self, authorization_code=None, refresh_token=None, headers=None):
        # Wraps get_token_hash for getting access token
        return self.get_token_hash(authorization_code, refresh_token, headers=headers or {})

    def get_refresh_token(self, authorization_code=None, headers=None):
        # Exchange authorization code for refresh token for future payments
        if self.token_hash is None:
            raise MissingConfig("Token hash needed to get new refresh token.")
        return self.get_token_hash(authorization_code, headers=headers or {}, refresh_token=self.token_hash)

    def logout(self):
        return self.delete("/v1/logout")

    def request(self, url, method, body=None, headers=None, refresh_token=None):
        """Make HTTP call, formats response and does error handling. Uses http_call method in API class.
        Usage::
            >>> api.request("https://api.sandbox.max-solutions.co/v1/cfdi?id=10", "GET", {})
            >>> api.request("https://api.sandbox.max-solutions.co/v1/cfdi/stamp", "POST", "{}", {} )
        """

        http_headers = merge_dict(self.headers(refresh_token=refresh_token, headers=headers or {}), headers or {})

        try:
            return self.http_call(url, method, data=json.dumps(body), headers=http_headers)

        # Format Error message for bad request
        # except BadRequest as error:
        #    return {"error": json.loads(error.content)}
        # Handle Expired token
        except UnauthorizedAccess as error:
            if self.token_hash and self.client_id:
                self.token_hash = None
                return self.request(url, method, body, headers)
            else:
                raise error

    def http_call(self, url, method, **kwargs):
        """Makes a http call. Logs response information.
        """
        error_tracking(info='Request[%s]: %s' % (method, url), log=log)

        if self.mode.lower() != 'live':
            request_headers = str(kwargs.get("headers", {}))
            request_body = str(kwargs.get("data", {}))
            error_tracking(log=log, debug="Level: " + self.mode)
            error_tracking(log=log, debug='Request: \nHeaders: %s\nBody: %s' % (request_headers, request_body))
        else:
            error_tracking(info='Not logging full request/response headers and body in live mode for compliance',
                           log=log)

        start_time = datetime.datetime.now()
        response = requests.request(method, url, **kwargs)
        duration = datetime.datetime.now() - start_time
        error_tracking(log=log, info='Response[%d]: %s, Duration: %s.%ss.' % (
            response.status_code, response.reason, duration.seconds, duration.microseconds))
        if self.mode.lower() != 'live':
            error_tracking(log=log, debug='Headers: %s\nBody: %s' % (str(response.headers), str(response.content)))
        return self.handle_response(response, response.content.decode('utf-8'))

    @classmethod
    def handle_response(cls, response, content):
        """Validate HTTP response
        """
        status = response.status_code
        if status in (301, 302, 303, 307):
            raise Redirection(response, content)
        elif 200 <= status <= 299:
            return json.loads(content) if content else {}
        elif status == 400:
            raise BadRequest(response, content)
        elif status == 401:
            raise UnauthorizedAccess(response, content)
        elif status == 403:
            raise ForbiddenAccess(response, content)
        elif status == 404:
            raise ResourceNotFound(response, content)
        elif status == 405:
            raise MethodNotAllowed(response, content)
        elif status == 409:
            raise ResourceConflict(response, content)
        elif status == 410:
            raise ResourceGone(response, content)
        elif status == 422:
            raise ResourceInvalid(response, content)
        elif 401 <= status <= 499:
            raise ClientError(response, content)
        elif 500 <= status <= 599:
            raise ServerError(response, content)
        else:
            raise ConnectionError(
                response, content, "Unknown response code: #{response.code}")

    def headers(self, refresh_token=None, headers=None):
        """Default HTTP headers
        """
        token_hash = self.get_token_hash(refresh_token=refresh_token, headers=headers or {})

        return {
            "Authorization": "Bearer %s" % token_hash,
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "User-Agent": self.user_agent
        }

    def get(self, action, headers=None, refresh_token=None):
        """Make GET request
        Usage::
            >>> api.get("v1/payments/payment?count=1")
            >>> api.get("v1/payments/payment/PAY-1234")
        """
        return self.request(join_url(self.endpoint, action), 'GET', headers=headers or {},
                            refresh_token=refresh_token)

    def post(self, action, params=None, headers=None, refresh_token=None):
        """Make POST request
        Usage::
            >>> api.post("v1/payments/payment", { 'indent': 'sale' })
            >>> api.post("v1/payments/payment/PAY-1234/execute", { 'payer_id': '1234' })
        """
        return self.request(join_url(self.endpoint, action), 'POST', body=params or {}, headers=headers or {},
                            refresh_token=refresh_token)

    def put(self, action, params=None, headers=None, refresh_token=None):
        """Make PUT request
        Usage::
            >>> api.put("v1/invoicing/invoices/INV2-RUVR-ADWQ", { 'id': 'INV2-RUVR-ADWQ', 'status': 'DRAFT'})
        """
        return self.request(join_url(self.endpoint, action), 'PUT', body=params or {}, headers=headers or {},
                            refresh_token=refresh_token)

    def patch(self, action, params=None, headers=None, refresh_token=None):
        """Make PATCH request
        Usage::
            >>> api.patch("v1/payments/billing-plans/P-5VH69258TN786403SVUHBM6A", { 'op': 'replace', 'path': '/merchant-preferences'})
        """
        return self.request(join_url(self.endpoint, action), 'PATCH', body=params or {}, headers=headers or {},
                            refresh_token=refresh_token)

    def delete(self, action, headers=None, refresh_token=None):
        """Make DELETE request
        """
        return self.request(join_url(self.endpoint, action), 'DELETE', headers=headers or {},
                            refresh_token=refresh_token)


__api__ = None


def default():
    """Returns default api object and if not present creates a new one
    By default points to developer sandbox
    """
    global __api__
    if __api__ is None:
        try:
            client_id = os.environ["INNOV_CLIENT_ID"]
            client_secret = os.environ["INNOV_CLIENT_SECRET"]
        except KeyError:
            raise MissingConfig("Required INNOV_CLIENT_ID and INNOV_CLIENT_SECRET")

        __api__ = Api(mode=os.environ.get("INNOV_MODE", "sandbox"), client_id=client_id, client_secret=client_secret)
    return __api__


def set_config(options=None, **config):
    """Create new default api object with given configuration
    """
    global __api__
    __api__ = Api(options or {}, **config)
    return __api__


configure = set_config
