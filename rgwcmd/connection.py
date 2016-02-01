"""Connections to a Ceph RADOS Gateway (radosgw) service."""

import requests
from awsauth import S3Auth

class Connection:

    def __init__(self, access_key, secret_key, server, port, is_secure=False):
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
        return '<%s:%s>' % (self.__class__.__name__, self.host)

    def get_base_url(self):
        '''Return a base URL.  eg. https://ceph.server'''
        return self._base_url
 
    def _get_request_url(self, endpoint):
        return '%s/%s' % (self._base_url, endpoint)

    def request(self, method, endpoint, **params):
        """Send requests to ceph-rgw."""
        response = requests.request(method=method, url=self._get_request_url(endpoint), auth=self.auth, params=params)
        return response
