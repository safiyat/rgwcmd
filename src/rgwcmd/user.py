"""User service for Ceph RADOS Gateway (radosgw)."""

class User:

    def __init__(self, uid='', display_name='', email='', access_key='',
                 secret_key='', user_caps='', max_buckets=1000, suspended=''):
        """User class constructor."""
        self._uid = uid
        self._display_name = display_name
        self._email = email
        self._access_key = access_key
        self._secret_key = secret_key
        self._user_caps = user_caps
        self._max_buckets = max_buckets
        self._suspended = suspended

    def build_params(self, uid='', display_name='', email='', access_key='',
                      secret_key='', user_caps='', max_buckets='', suspended='',
                      purge_data=''):
        """Function to build the parameters supplied"""
        param_string = ''

        if uid:
            param_string += 'uid=' + uid + '&'

        if display_name:
            param_string += 'display-name=' + display_name + '&'

        if email:
            param_string += 'email=' + email + '&'


        if access_key:
            param_string += 'access-key=' + access_key + '&'

        if secret_key:
            param_string += 'secret-key=' + secret_key + '&'


        if user_caps:
            param_string += 'user-caps=' + user_caps + '&'

        if max_buckets:
            param_string += 'max-buckets=' + str(max_buckets) + '&'

        if suspended:
            param_string += 'suspended=' + suspended + '&'

        if purge_data:
            param_string += 'purge-data=' + purge_data + '&'

        param_string += 'format=json'

        return param_string

    def check_params(self, param_string):
        pass


    def create_user(self, uid, display_name, email='', access_key='',
                    secret_key='', user_caps='', max_buckets=1000, suspended=''):
        """Create a new user. By default, an S3 key pair will be created automatically."""
        # if access_key and secret_key:
        method = 'PUT'
        endpoint = '/admin/user'
        params = self.build_params(uid=uid, display_name=display_name, email=email,
                               access_key=access_key, secret_key=secret_key,
                               user_caps=user_caps, max_buckets=max_buckets,
                               suspended=suspended)

        return method, endpoint, params


    def update_user(self, uid, display_name='', email='', access_key='',
                    secret_key='', user_caps='', max_buckets=1000, suspended=''):
        """Update a user."""
        # if access_key and secret_key:
        method = 'POST'
        endpoint = '/admin/user'
        params = self.build_params(uid=uid, display_name=display_name, email=email,
                               access_key=access_key, secret_key=secret_key,
                               user_caps=user_caps, max_buckets=max_buckets,
                               suspended=suspended)

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
