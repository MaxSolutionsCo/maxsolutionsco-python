# -*- coding: utf-8 -*-
# © Yonn, Xyz. All rights reserved.
import json


class ErrorConnection(Exception):

    def __init__(self, response, content=None, message=None):
        self.response = response
        self.content = json.loads(content)
        if message is None:
            self.message = self.content.get('Message', None)
        else:
            self.message = message

    def __str__(self):
        message = "Failed."
        if hasattr(self.response, 'status_code'):
            message += " Response status: %s." % (self.response.status_code)
        if hasattr(self.response, 'reason'):
            message += " Response message: %s." % (self.response.reason)
        if self.message is not None:
            message += " Error message: " + str(self.message)
        return message


class Redirection(ErrorConnection):
    """3xx Redirection
    """
    def __str__(self):
        message = super(Redirection, self).__str__()
        if self.response.get('Location'):
            message = "%s => %s" % (message, self.response.get('Location'))
        return message


class MissingParam(TypeError):
    pass


class MissingConfig(Exception):
    pass


class InvalidConfig(ValueError):
    pass


class ClientError(ErrorConnection):
    """4xx Client Error
    """
    pass


class BadRequest(ClientError):
    """400 Bad Request
    """
    pass


class UnauthorizedAccess(ClientError):
    """401 Unauthorized
    """
    pass


class ForbiddenAccess(ClientError):
    """403 Forbidden
    """
    pass


class ResourceNotFound(ClientError):
    """404 Not Found
    """
    pass


class ResourceConflict(ClientError):
    """409 Conflict
    """
    pass


class ResourceGone(ClientError):
    """410 Gone
    """
    pass


class ResourceInvalid(ClientError):
    """422 Invalid
    """
    pass


class ServerError(ErrorConnection):
    """5xx Server Error
    """
    pass


class MethodNotAllowed(ClientError):
    """405 Method Not Allowed
    """

    def allowed_methods(self):
        """
        Implement this method return method allow
        :return:
        """
        # return self.response['Allow']
        pass
