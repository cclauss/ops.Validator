from django.http import HttpResponse

from openstack_auth.exceptions import KeystoneAuthException


class KeystoneAuthExceptionMiddleware(KeystoneAuthException):
    def process_exception(self, request, exception):
        if (isinstance(exception, KeystoneAuthException) and exception.message == u"Invalid credentials."):
            return HttpResponse('Unauthorized', status=401)


