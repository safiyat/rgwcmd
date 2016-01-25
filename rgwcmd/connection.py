"""Connections to a Ceph RADOS Gateway (radosgw) service."""

import json
import urllib
import boto.connection
import boto.s3.connection

import radosgw.exception
from radosgw.user import UserInfo

class RadosGWAdminConnection(boto.connection.AWSAuthConnection):
    """CEPH RADOS Gateway (radosgw) admin operations connection.
    :see: http://ceph.com/docs/next/radosgw/adminops/
    """
    def __init__(self,
                 access_key, secret_key,
                 host,
                 admin_path='/admin',
                 is_secure=True, port=None,
                 proxy=None, proxy_port=None, proxy_user=None, proxy_pass=None,
                 debug=0,
                 https_connection_factory=None, security_token=None,
                 validate_certs=True):
        """Constructor."""

        self.admin_path = admin_path
        boto.connection.AWSAuthConnection.__init__(self,
                                                   host=host,
                                                   aws_access_key_id=access_key,
                                                   aws_secret_access_key=secret_key,
                                                   is_secure=is_secure, port=port,
                                                   proxy=proxy, proxy_port=proxy_port,
                                                   proxy_user=proxy_user, proxy_pass=proxy_pass,
                                                   debug=debug,
                                                   https_connection_factory=https_connection_factory,
                                                   path=self.admin_path,
                                                   provider='aws',
                                                   security_token=security_token,
                                                   suppress_consec_slashes=True,
                                                   validate_certs=validate_certs)
