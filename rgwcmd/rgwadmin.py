"""User service for Ceph RADOS Gateway (radosgw)."""

from exceptions import *

import connection
import rgwconfig
import colors

def init_connection():
    rgwconf = rgwconfig.rgwconfig()
    host, access_key, secret_key = rgwconf.read_conf()
    conn = connection.Connection(host, access_key, secret_key)

conn = init_connection()

class adminutils(object):

    @staticmethod
    def _print_response_msg(code, message):
        #(navneet) This method will be called by all static methods to print response to user.
        if 200 <= code < 300:
            print Colors.BOLD + Colors.GREEN + "%d" % code + Colors.ENDC
            print message
            return
        if 400 <= code < 500:
            print Colors.BOLD + Colors.RED + "%d" % code + Colors.ENDC
            print message
            return
        if 500 <= code:
            print Colors.BOLD + Colors.YELLOW + "%d" % code + Colors.ENDC
            print message
            return

    @staticmethod
    def create_user(uid, display_name, email=None, key_type='s3',
                    access_key=None, secret_key=None, user_caps=None,
                    generate_key=True, max_buckets=1000, suspended=False):
        """Create a new user. By default, an S3 key pair will be created\
           automatically."""

        if access_key and secret_key:
            generate_key = False
        elif access_key or secret_key:
            raise MissingKeys
        else:
            generate_key = True

        endpoint = '/admin/user'
        return conn.request_ok(method='PUT', endpoint=endpoint, uid=uid,
                               display_name=display_name,
                               key_type=key_type, email=email,
                               access_key=access_key,
                               secret_key=secret_key, user_caps=user_caps,
                               generate_key=generate_key,
                               max_buckets=max_buckets,
                               suspended=suspended)

    @staticmethod
    def update_user(uid, display_name=None, email=None, access_key=None,
                    secret_key=None, generate_key=None, user_caps=None,
                    max_buckets=1000, suspended=None):
        """Update a user."""

        if access_key and secret_key:
            generate_key = False
        elif access_key or secret_key:
            raise MissingKeys
        else:
            generate_key = True

        endpoint = '/admin/user'
        return conn.request_ok(method='POST', endpoint=endpoint, uid=uid,
                               display_name=display_name,
                               key_type=key_type, email=email,
                               access_key=access_key,
                               secret_key=secret_key, user_caps=user_caps,
                               generate_key=generate_key,
                               max_buckets=max_buckets,
                               suspended=suspended)

    @staticmethod
    def remove_user(uid, purge_data=None):
        """Delete a user."""
        endpoint = '/admin/user'
        return conn.request_ok(method='DELETE', endpoint=endpoint,
			       uid=uid, purge_data=purge_data)

    @staticmethod
    def add_key(uid, access_key=None, secret_key=None):
        """Add a key-pair for a user"""
        if access_key and secret_key:
            generate_key = False
        elif access_key or secret_key:
            raise MissingKeys
        else:
            generate_key = True

        endpoint = '/admin/user'
        return conn.request_ok(method='PUT', endpoint=endpoint, uid=uid,
                               access_key=access_key, secret_key=secret_key,
                               generate_key=generate_key)

    @staticmethod
    def remove_key(uid, access_key):
        """Remove a key-pair from a user"""
        endpoint = '/admin/user'
        return conn.request_ok(method='DELETE', endpoint=endpoint, uid=uid, access_key=access_key)

    @staticmethod
    def add_caps(uid, user_caps):
        """Add an administrative capability to a specified user."""
        endpoint = '/admin/user'
        return conn.request_ok(method='PUT', endpoint=endpoint, uid=uid, user_caps=user_caps)

    @staticmethod
    def remove_caps(uid, user_caps):
        """Remove an administrative capability from a specified user."""
        endpoint = '/admin/user'
        return conn.request_ok(method='DELETE', endpoint=endpoint, uid=uid, user_caps=user_caps)
