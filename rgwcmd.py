#! /usr/bin/env python

import ConfigParser
import os

from rgwcmd import argparsen
from rgwcmd.user import User
from rgwcmd.connection import Connection
from rgwcmd.utils import *
from rgwcmd.commands import *


def write_conf(host, access_key, secret_key):
    conf = ConfigParser.ConfigParser()

    conf.add_section('rgwadmin')
    conf.set('rgwadmin', 'host', host)
    conf.set('rgwadmin', 'access-key', access_key)
    conf.set('rgwadmin', 'secret-key', secret_key)

    with open(os.environ['HOME'] + '/.rgwadmin', 'w') as configfile:
        conf.write(configfile)


def read_conf():
    conf = ConfigParser.ConfigParser()
    conf.read(os.environ['HOME'] + '/.rgwadmin')

    host = conf.get('rgwadmin', 'host')
    access_key = conf.get('rgwadmin', 'access-key')
    secret_key = conf.get('rgwadmin', 'secret-key')

    return host, access_key, secret_key

if __name__ == '__main__':

    if os.path.isfile(os.environ['HOME'] + '/.rgwadmin'):
        host, access_key, secret_key = read_conf()
        conn = Connection(access_key=access_key, secret_key=secret_key,
                          server=host, port=80)
    else:
        print "No config file found at '%s'" % (os.environ['HOME']
                                                + '/.rgwadmin')
        print "Entering one time configuration..."
        host = raw_input("    Rados Gateway Server:")
        access_key = raw_input("    Access Key:")
        secret_key = raw_input("    Secret Key:")
        write_conf(host=host, access_key=access_key, secret_key=secret_key)
        conn = Connection(access_key=access_key, secret_key=secret_key,
                          server=host)

    parser = argparsen.ArgumentParser(description = 'Ceph Rados Gateway REST\
                                                     API on the cmd.')
    subparsers = parser.add_subparsers(dest="command")

    # Iterates over user, keys, caps
    for command in command_list['commands']:
        command_parser = subparsers.add_parser(command.keys()[0])
        # Iterates over subcommands, function and dest
        for key, value in command.iteritems():
            command_parser.set_defaults(func=value['function'])
            subparsers = command_parser.add_subparsers(dest=value['dest'])
            # Iterates over create, update, rm, info; etc
            for command in value['subcommands']:
                command_parser = subparsers.add_parser(command.keys()[0])
                # Iterates over a single entry in the dictionary:arguments
                for command, properties  in command.iteritems():
                    # Iterates over arguments to a single command: uid, email...
                    for argument in properties['arguments']:
                        # Iterates over kv pairs in arguments:short,long,type...
                        for key, value in argument.iteritems():
                            print value['dest']
                            command_parser.add_argument(value['short'],
                                                        value['long'],
                                                        type=value['type'],
                                                        required=
                                                        value['required'],
                                                        help=value['help'],
                                                        metavar=
                                                        value['metavar'],
                                                        dest=value['dest'])



    args = parser.parse_args()
    args.func(args)



########################## Pure Genius. Never delete. ##########################
################################################################################
# command_list = {                                                             #
#     "user": {                                                                #
#         "create": {                                                          #
#             "foo": []                                                        #
#         }                                                                    #
#     }                                                                        #
# }                                                                            #
# parser = argparse.ArgumentParser(description=                                #
#                                  'Ceph Rados Gateway REST API on the cmd.')  #
# subparsers = parser.add_subparsers(dest="command")                           #
#                                                                              #
# for command, subcommands in command_list.iteritems():                        #
#     command_parser = subparsers.add_parser(command)                          #
#     subcommand_parser = command_parser.add_subparsers(dest="subcommand")     #
#     for subcommand, arguments in subcommands.iteritems():                    #
#         p = subcommand_parser.add_parser(subcommand)                         #
#         p.set_defaults(func=foo)                                             #
#         for argument, helper in arguments.iteritems():                       #
#             p.add_argument(argument)                                         #
################################################################################
#######################author: yagnik.khanna@snapdeal.com#######################
