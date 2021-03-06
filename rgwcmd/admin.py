"""User service for Ceph RADOS Gateway (radosgw)."""

from exceptions import *

import connection
import config
import colors

def init_connection(path=None):
    rgwconf = config.ConfigHelper(path=path)
    host, access_key, secret_key = rgwconf.get_conf()
    conn = connection.Connection(host, access_key, secret_key)
    return conn

class AdminUtils(object):

    @staticmethod
    def _print_response_msg(code, message):
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
    def configure():
        rgwconf = config.ConfigHelper()
        rgwconf.init_config()

    @staticmethod
    def create_user(uid, display_name, email=None, key_type=None,
                    access_key=None, secret_key=None, user_caps=None,
                    generate_key=None, max_buckets=None, suspended=None,
                    path=None):
        """Create a new user. By default, an s3 key pair will be created\
           automatically."""

        if access_key and secret_key:
            generate_key = False
        elif access_key or secret_key:
            raise MissingKeys
        elif generate_key == 'Y' or generate_key == 'y':
            generate_key = True
        elif generate_key == 'N' or generate_key == 'n':
            generate_key = False
        else:
            generate_key = None


        if suspended == 'Y' or suspended == 'y':
            suspended = True
        elif suspended == 'N' or suspended == 'n':
            suspended = False
        else:
            suspended = None

        endpoint = '/admin/user'
        return init_connection(path=path).request_ok(method='PUT',
                                                     endpoint=endpoint, uid=uid,
                                                     display_name=display_name,
                                                     key_type=key_type,
                                                     email=email,
                                                     access_key=access_key,
                                                     secret_key=secret_key,
                                                     user_caps=user_caps,
                                                     generate_key=generate_key,
                                                     max_buckets=max_buckets,
                                                     suspended=suspended)

    @staticmethod
    def update_user(uid, display_name=None, email=None, key_type=None,
                    access_key=None, secret_key=None, generate_key=None,
                    user_caps=None, max_buckets=None, suspended=None,
                    path=None):
        """Update a user."""

        if access_key and secret_key:
            generate_key = False
        elif access_key or secret_key:
            raise MissingKeys
        elif generate_key == 'Y' or generate_key == 'y':
            generate_key = True
        elif generate_key == 'N' or generate_key == 'n':
            generate_key = False
        else:
            generate_key = None

        if suspended == 'Y' or suspended == 'y':
            suspended = True
        elif suspended == 'N' or suspended == 'n':
            suspended = False
        else:
            suspended = None

        endpoint = '/admin/user'
        return init_connection(path=path).request_ok(method='POST',
                                                     endpoint=endpoint, uid=uid,
                                                     display_name=display_name,
                                                     key_type=key_type,
                                                     email=email,
                                                     access_key=access_key,
                                                     secret_key=secret_key,
                                                     user_caps=user_caps,
                                                     generate_key=generate_key,
                                                     max_buckets=max_buckets,
                                                     suspended=suspended)

    @staticmethod
    def remove_user(uid, purge_data=None, path=None):
        """Delete a user."""
        endpoint = '/admin/user'
        return init_connection(path=path).request_ok(method='DELETE',
                                                     endpoint=endpoint, uid=uid,
                                                     purge_data=purge_data)
    @staticmethod
    def info_user(uid, path=None):
        """Delete a user."""
        endpoint = '/admin/user'
        return init_connection(path=path).request_ok(method='GET',
                                                     endpoint=endpoint, uid=uid)

    @staticmethod
    def add_key(uid, access_key=None, secret_key=None, generate_key=None,
                path=None):
        """Add a key-pair for a user"""
        if access_key and secret_key:
            generate_key = False
        elif access_key or secret_key:
            raise MissingKeys
        else:
            generate_key = True

        endpoint = '/admin/user?key'
        return init_connection(path=path).request_ok(method='PUT',
                                                     endpoint=endpoint, uid=uid,
                                                     access_key=access_key,
                                                     secret_key=secret_key,
                                                     generate_key=generate_key)

    @staticmethod
    def remove_key(access_key, uid=None, path=None):
        """Remove a key-pair from a user"""
        endpoint = '/admin/user?key'
        return init_connection(path=path).request_ok(method='DELETE',
                                                     endpoint=endpoint, uid=uid,
                                                     access_key=access_key)

    @staticmethod
    def add_caps(uid, user_caps, path=None):
        """Add an administrative capability to a specified user."""
        endpoint = '/admin/user?caps'
        return init_connection(path=path).request_ok(method='PUT',
                                                     endpoint=endpoint, uid=uid,
                                                     user_caps=user_caps)

    @staticmethod
    def remove_caps(uid, user_caps, path=None):
        """Remove an administrative capability from a specified user."""
        endpoint = '/admin/user?caps'
        return init_connection(path=path).request_ok(method='DELETE',
                                                     endpoint=endpoint, uid=uid,
                                                     user_caps=user_caps)
