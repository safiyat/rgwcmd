"""Connections to a Ceph RADOS Gateway (radosgw) service."""

import requests
from awsauth import S3Auth

class Connection:

    def __init__(self, access_key, secret_key, server, is_secure=False):
        self._access_key = access_key
        self._secret_key = secret_key
        self._server = server
        if is_secure:
            self._protocol = 'https'
        else:
            self._protocol = 'http'

        self.auth = S3Auth(access_key = self._access_key, secret_key = self._secret_key, server=self._server)


    def get_base_url(self):
        '''Return a base URL.  eg. https://ceph.server'''
        return '%s://%s' % (self._protocol, self._server)
