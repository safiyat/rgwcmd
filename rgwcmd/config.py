import ConfigParser
import os

class ConfigHelper(object):

    def __init__(self, path=None):
        if not path:
	    self.path = os.environ['HOME'] + '/.rgwadmin'
        else:
	    self.path = path
        self.conf = ConfigParser.ConfigParser()

    def write_conf(self, host, access_key, secret_key):
        self.conf.add_section('rgwadmin')
        self.conf.set('rgwadmin', 'host', host)
        self.conf.set('rgwadmin', 'access-key', access_key)
        self.conf.set('rgwadmin', 'secret-key', secret_key)
        with open(self.path, 'w') as configfile:
            self.conf.write(configfile)

    def read_conf(self):
        self.conf.read(self.path)
        host = self.conf.get('rgwadmin', 'host')
        access_key = self.conf.get('rgwadmin', 'access-key')
        secret_key = self.conf.get('rgwadmin', 'secret-key')
        return host, access_key, secret_key

    def get_conf(self):
        if os.path.isfile(self.path):
            return self.read_conf()
        print 'ERROR: Config file not found at /home/safiyat/.rgwadmin. Please'\
               'run `config edit\' first.'
        exit()

    def init_config(self):
        print 'Storing configuration at path %s' % self.path
        print 'Please enter the rgwadmin configuration...'
        host = raw_input('    Rados Gateway Server:')
        access_key = raw_input('    Access Key:')
        secret_key = raw_input('    Secret Key:')
        self.write_conf(host=host, access_key=access_key, secret_key=secret_key)
