"""User service for Ceph RADOS Gateway (radosgw)."""

class User(object):

    def __init__(self):
        """User class constructor."""
        pass

    def check_params(self, param_string):
        pass

    def create_user(self, uid, display_name, email=None, key_type='s3', access_key=None,
                    secret_key=None, user_caps=None, generate_key=True, max_buckets=1000,
                    suspended=False):
        """Create a new user. By default, an S3 key pair will be created automatically."""
        endpoint = '/admin/user'
        response = self._conn.request(method='PUT', endpoint, uid=uid, display_name=display_name,
                                      key_type=key_type, email=email, access_key=access_key,
                                      secret_key=secret_key, user_caps=user_caps,
                                      generate_key=generate_key,
                                      max_buckets=max_buckets, suspended=suspended)
        # parse response

    def update_user(self, uid, display_name='', email='', access_key='',
                    secret_key='', generate_key='', user_caps='',
                    max_buckets=1000, suspended=''):
        """Update a user."""
        # if access_key and secret_key:
        method = 'POST'
        endpoint = '/admin/user'
        params = self.build_params(uid=uid, display_name=display_name, email=email,
                               access_key=access_key, secret_key=secret_key,
                               user_caps=user_caps, max_buckets=max_buckets,
                               suspended=suspended)
        if generate_key:
            params = 'generate-key=True&' + self.build_params(uid=uid)

        return method, endpoint, params


    def remove_user(self, uid, purge_data=''):
        """Delete a user."""
        method = 'DELETE'
        endpoint = '/admin/user'
        params = self.build_params(uid=uid, purge_data=purge_data)

        return method, endpoint, params


    def add_key(self, uid, access_key='', secret_key='', generate_key=''):
        """Add a key-pair for a user"""
        if generate_key:
            params = 'generate-key=True&' + self.build_params(uid=uid)
        else:
            params = self.build_params(uid=uid, access_key=access_key, secret_key=secret_key)

        method = 'PUT'
        endpoint = '/admin/user'
        params = 'key&' + params

        return method, endpoint, params


    def remove_key(self, access_key, uid=''):
        """Remove a key-pair from a user"""

        method = 'DELETE'
        endpoint = '/admin/user'
        params = 'key&' + self.build_params(uid=uid, access_key=access_key)

        return method, endpoint, params


    def add_caps(self, uid, user_caps):
        """Add an administrative capability to a specified user."""

        method = 'PUT'
        endpoint = '/admin/user'
        params = 'caps&' + self.build_params(uid=uid, user_caps=user_caps)

        return method, endpoint, params


    def remove_caps(self, uid, user_caps):
        """Remove an administrative capability from a specified user."""

        method = 'DELETE'
        endpoint = '/admin/user'
        params = 'caps&' + self.build_params(uid=uid, user_caps=user_caps)

        return method, endpoint, params
