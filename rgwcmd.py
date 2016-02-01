#! /usr/bin/env python

import ConfigParser
import os

from rgwcmd import argparsen
from rgwcmd.user import User
from rgwcmd.connection import Connection
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


def user_func(args):
    if args.subcommand == 'create':
        usr = User()
        method, endpoint, params = usr.create_user(uid=args.uid,
                                                   display_name=args.dispname,
                                                   email=args.email,
                                                   access_key=args.access_key,
                                                   secret_key=args.secret_key,
                                                   user_caps=args.caps,
                                                   max_buckets=args.max_buckets,
                                                   suspended=args.suspend)
        response = conn.request(method=method, endpoint=endpoint, params=params)
        if response.status_code == 200:
            print "OK"
        print response.text


    if args.subcommand == 'rm':
        usr = User()
        method, endpoint, params = usr.remove_user(uid=args.uid,
                                                   purge_data=args.purge)
        response = conn.request(method=method, endpoint=endpoint, params=params)
        if response.status_code == 200:
            print "OK"
        print response.text

    if args.subcommand == 'update':
        usr = User()
        method, endpoint, params = usr.update_user(uid=args.uid,
                                                   display_name=args.dispname,
                                                   email=args.email,
                                                   access_key=args.access_key,
                                                   secret_key=args.secret_key,
                                                   generate_key=args.gen_key,
                                                   user_caps=args.caps,
                                                   max_buckets=args.max_buckets,
                                                   suspended=args.suspend)
        response = conn.request(method=method, endpoint=endpoint, params=params)
        if response.status_code == 200:
            print "OK"
        print response.text

    if args.subcommand == 'info':
        usr = User()
        method, endpoint, params = usr.update_user(uid=args.uid)
        method = 'GET'
        response = conn.request(method=method, endpoint=endpoint, params=params)
        if response.status_code == 200:
            print "OK"
        print response.text

def key_func(args):
    if args.subcommand == 'add':
        usr = User()
        method, endpoint, params = usr.add_key(uid=args.uid,
                                               access_key=args.access_key,
                                               secret_key=args.secret_key,
                                               generate_key=args.gen_key)
        response = conn.request(method=method, endpoint=endpoint, params=params)
        if response.status_code == 200:
            print "OK"
        print response.text

    if args.subcommand == 'rm':
        usr = User()
        method, endpoint, params = usr.remove_key(access_key=args.access_key,
                                                  uid=args.uid)
        response = conn.request(method=method, endpoint=endpoint, params=params)
        if response.status_code == 200:
            print "OK"
        print response.text


def caps_func(args):
    if args.subcommand == 'add':
        usr = User()
        method, endpoint, params = usr.add_caps(uid=args.uid,
                                                user_caps=args.caps)
        response = conn.request(method=method, endpoint=endpoint, params=params)
        if response.status_code == 200:
            print "OK"
        print response.text

    if args.subcommand == 'rm':
        usr = User()
        method, endpoint, params = usr.remove_caps(uid=args.uid,
                                                user_caps=args.caps)
        response = conn.request(method=method, endpoint=endpoint, params=params)
        if response.status_code == 200:
            print "OK"
        print response.text



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
