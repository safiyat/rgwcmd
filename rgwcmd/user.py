"""User service for Ceph RADOS Gateway (radosgw)."""

import requests
from awsauth import S3Auth

class User:

    def __init__(self, uid):
        """ """
        self._uid = uid


    def
