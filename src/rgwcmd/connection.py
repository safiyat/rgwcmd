"""Connections to a Ceph RADOS Gateway (radosgw) service."""

import requests, urllib
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

        self.auth = S3Auth(access_key = self._access_key, secret_key = self._secret_key)

    def __repr__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.host)

    def get_base_url(self):
        '''Return a base URL.  eg. https://ceph.server'''
        return '%s://%s' % (self._protocol, self._server)

    # def build_base_http_request(self, method, path, auth_path,
    #                             params=None, headers=None, data='', host=None):
    #     path = self.get_path(path)
    #     if auth_path is not None:
    #         auth_path = self.get_path(auth_path)
    #     if params is None:
    #         params = {}
    #     else:
    #         params = params.copy()
    #     if headers is None:
    #         headers = {}
    #     else:
    #         headers = headers.copy()
    #     if self.host_header and not boto.utils.find_matching_headers('host', headers):
    #         headers['host'] = self.host_header
    #     host = host or self.host
    #     if self.use_proxy:
    #         if not auth_path:
    #             auth_path = path
    #         path = self.prefix_proxy_to_path(path, host)
    #         if self.proxy_user and self.proxy_pass and not self.is_secure:
    #             # If is_secure, we don't have to set the proxy authentication
    #             # header here, we did that in the CONNECT to the proxy.
    #             headers.update(self.get_proxy_auth_header())
    #     return HTTPRequest(method, self.protocol, host, self.port,
    #                        path, auth_path, params, headers, data)

    # def make_request(self, method, path, query_params=None, headers=None, data='', host=None,
    #                  sender=None, override_num_retries=None, retry_handler=None):
    #     """Makes a request to the RADOS GW admin server.
    #     :param str method: GET|PUT|HEAD|POST|DELETE|...
    #     :param str path: admin sub request path (i.e. /user)
    #     :param dict query_params: url query parameters
    #     :returns boto.connection.HttpResponse: the HTTP response
    #     """
    #     auth_path = path
    #     if not query_params:
    #         query_params = {}
    #     else:
    #         query = urllib.urlencode(query_params)
    #         auth_path = auth_path + '?' + query
    #     http_request = self.build_base_http_request(method, path, auth_path,
    #                                                 query_params, headers, data, host)
    #     return self._mexe(http_request, sender, override_num_retries,
    #                       retry_handler=retry_handler)

    def request(self, method, endpoint, params):
        """Send requests to ceph-rgw."""

        url = self.get_base_url() + endpoint + '?' + params
        response = requests.request(method=method, url=url, auth=self.auth)

        return response
