import affectr
import json
import requests

class HttpRequest(object):

    def __init__(self, method, url):
        self._method = method
        self._url = url
        headers = {}
        headers["Accept"] = "application/json"
        lib_version = affectr.get_version()
        headers["User-Agent"] = "affectr-python/{0}".format(lib_version)
        self._opts = {"headers": headers}

        if not self._valid_method(method):
            raise ValueError('Invalid method {0}'.format(method))

    def _valid_method(self, method):
        return method in ('get', 'post', 'put', 'delete')

    def use_http_auth(self, username, password):
        self._opts['auth'] = (username, password)

    def set_payload(self, payload):
        if payload is not None:
            # Set the payload type - always JSON
            self._opts['headers']['Content-Type'] = 'application/json'
            # And JSON encode the data
            self._opts['data'] = json.dumps(payload)

    def perform(self):
        fetch_func = getattr(requests, self._method)
        response = fetch_func(self._url, **self._opts)
        return json.loads(response.content)

