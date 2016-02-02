import ConfigParser
import os


class rgwconfig(object):

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

   #(navneet) Can add another method to check for existence of file and give useful message to user.
