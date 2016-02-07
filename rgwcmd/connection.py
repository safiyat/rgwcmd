"""Connections to a Ceph RADOS Gateway (radosgw) service."""

import requests
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

    def request_ok(self, method, endpoint, **params):
	response = self._request(method, endpoint, **params)
        print response.text
        print response.status_code
        return self._parse_response(response)

    def _request(self, method, endpoint, **params):
        """Send requests to ceph-rgw."""
        print "%s\n%s\n%s\n\n" % (method, self._get_request_url(endpoint), params)
        response = requests.request(method=method, url=self._get_request_url(endpoint), auth=self.auth, params=params)
        return response

    def _parse_response(self, response):
        """Parse the response of Connection.request function"""
        #(navneet) check for return codes and raise exceptions with a message
        # Can't be done. eg. NoSuchUser NoSuchBucket NoSuchKey all return 404.
        code = response.status_code
        text = response.text
        return code, text
