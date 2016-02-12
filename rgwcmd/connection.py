"""Connections to a Ceph RADOS Gateway (radosgw) service."""

import requests
import json
from awsauth import S3Auth

class Connection(object):

    def __init__(self, server, access_key, secret_key, is_secure=False):
        self._access_key = access_key
        self._secret_key = secret_key
        self._server = server
        if is_secure:
            self._protocol = 'https'
        else:
            self._protocol = 'http'
        self.auth = S3Auth(access_key = self._access_key, secret_key = self._secret_key)
        self._base_url = '%s://%s' % (self._protocol, self._server)

    def __repr__(self):
        return '<%s:%s>' % (self.__class__.__name__, self._server)

    def get_base_url(self):
        '''Return a base URL.  eg. https://ceph.server'''
        return self._base_url

    def _get_request_url(self, endpoint):
        return '%s%s' % (self._base_url, endpoint)

    def _sanitize_request_params(self, params):
        for k in params.keys():
            if params.get(k) is None:
                params.pop(k)

    def request_ok(self, method, endpoint, **params):
        self._sanitize_request_params(params)
        for key in params.keys():
            oldkey = key
            newkey = oldkey.replace('_', '-')
            if oldkey != newkey:
                params[newkey] = params.pop(oldkey)
        params['format']='json'

	response = self._request(method, endpoint, **params)
        print json.dumps(json.loads(response.text), indent=4)
        print response.status_code
        return self._parse_response(response)

    def _request(self, method, endpoint, **params):
        """Send requests to ceph-rgw."""
        response = requests.request(method=method,
                                    url=self._get_request_url(endpoint),
                                    auth=self.auth, params=params)
        return response

    def _parse_response(self, response):
        """Parse the response of Connection.request function"""
        code = response.status_code
        text = response.text
        return code, text
