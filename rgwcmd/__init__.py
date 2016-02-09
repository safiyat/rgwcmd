"""Ceph RADOS Gateway (radosgw) admin operations."""

__version__ = '0.2'
__author__ = 'md.reza@snapdeal.com'

from . import commands

def get_version():
    """ Return the current version"""
    return __version__

def main():
    parser = commands.init_command_parser()
    args = parser.parse_args()
    args.func(**commands.namespace_to_dict(args))

if __name__ == '__main__':
    main()
