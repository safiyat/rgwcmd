#! /usr/bin/env python

from rgwcmd import argparsen

import requests
import json
# if __name__ == '__main__':

def user_func(args):
    if args.subcommand == 'create':
        print 'user create'

    if args.subcommand == 'rm':
        print 'user rm'

    if args.subcommand == 'update':
        print 'user update'


def key_func(args):
    if args.subcommand == 'add':
        print 'key add'

    if args.subcommand == 'rm':
        print 'key rm'


def caps_func(args):
    if args.subcommand == 'add':
        print 'caps add'

    if args.subcommand == 'rm':
        print 'caps rm'


parser = argparsen.ArgumentParser(description='Ceph Rados Gateway REST API on the cmd.')
subparsers = parser.add_subparsers(dest='command')

user_parser = subparsers.add_parser('user')
user_parser.set_defaults(func=user_func)
key_parser = subparsers.add_parser('key')
key_parser.set_defaults(func=key_func)
caps_parser = subparsers.add_parser('caps')
caps_parser.set_defaults(func=caps_func)

user_subparsers = user_parser.add_subparsers(dest='subcommand')
key_subparsers = key_parser.add_subparsers(dest='subcommand')
caps_subparsers = caps_parser.add_subparsers(dest='subcommand')


user_create_parser = user_subparsers.add_parser('create')
user_update_parser = user_subparsers.add_parser('update')
user_rm_parser = user_subparsers.add_parser('rm')

key_add_parser = key_subparsers.add_parser('add')
key_rm_parser = key_subparsers.add_parser('rm')

caps_add_parser = caps_subparsers.add_parser('add')
caps_rm_parser = caps_subparsers.add_parser('rm')


# for temp_parser in user_create_parser, user_update_parser, user_rm_parser:
#     temp_parser.add_argument('-u', '--uid', type=str, required=True,
#                              help='The user ID to be created/removed/updated.',
#                              metavar='johhny', dest='uid')

user_create_parser.add_argument('-u', '--uid', type=str, required=True,
                             help='The user ID to be created.',
                             metavar='johnny', dest='uid')
user_create_parser.add_argument('-d', '--display-name', type=str, required=True,
                             help='The display name of the user to be created.',
                             metavar='"Johnny Lever"', dest='dispname')
user_create_parser.add_argument('-e', '--email', type=str, required=False,
                             help='The email address associated with the user.',
                             metavar='lever.johhny@example.com', dest='email')
user_create_parser.add_argument('-a', '--access-key', type=str, required=False,
                             help='Specify access key.',
                             metavar='ABCD0EF12GHIJ2K34LMN', dest='access_key')
user_create_parser.add_argument('-s', '--secret-key', type=str, required=False,
                             help='Specify secret key.',
                             metavar='0AbCDEFg1h2i34JklM5nop6QrSTUV+WxyzaBC7D8',
                             dest='secret_key')
user_create_parser.add_argument('-c', '--caps', type=str, required=False,
                             help='User capabilities.',
                             metavar='"[users|buckets|metadata|usage|zone]=[*|read|write|read, write]"',
                             dest='caps')
user_create_parser.add_argument('-g', '--generate-key', type=str, required=False,
                             help='Generate a new key pair and add to the existing keyring.',
                             metavar='True', dest='gen_key')
user_create_parser.add_argument('-m', '--max-buckets', type=str, required=False,
                             help='Specify the maximum number of buckets the user can own.',
                             metavar='500', dest='max_buckets')
user_create_parser.add_argument('-x', '--suspend', type=str, required=False,
                             help='Specify whether the user should be suspended.',
                             metavar='False', dest='suspend')


user_update_parser.add_argument('-u', '--uid', type=str, required=True,
                             help='The user ID to be modified.',
                             metavar='johnny', dest='uid')
user_update_parser.add_argument('-d', '--display-name', type=str, required=False,
                             help='The display name of the user to be modified.',
                             metavar='"Johnny Lever"', dest='dispname')
user_update_parser.add_argument('-e', '--email', type=str, required=False,
                             help='The email address to be associated with the user.',
                             metavar='lever.johhny@example.com', dest='email')
user_update_parser.add_argument('-a', '--access-key', type=str, required=False,
                             help='Specify access key.',
                             metavar='ABCD0EF12GHIJ2K34LMN', dest='access_key')
user_update_parser.add_argument('-s', '--secret-key', type=str, required=False,
                             help='Specify secret key.',
                             metavar='0AbCDEFg1h2i34JklM5nop6QrSTUV+WxyzaBC7D8',
                             dest='secret_key')
user_update_parser.add_argument('-c', '--caps', type=str, required=False,
                             help='User capabilities.',
                             metavar='"[users|buckets|metadata|usage|zone]=[*|read|write|read, write]"',
                             dest='caps')
user_update_parser.add_argument('-g', '--generate-key', type=str, required=False,
                             help='Generate a new key pair and add to the existing keyring.',
                             metavar='True', dest='gen_key')
user_update_parser.add_argument('-m', '--max-buckets', type=str, required=False,
                             help='Specify the maximum number of buckets the user can own.',
                             metavar='500', dest='max_buckets')
user_update_parser.add_argument('-x', '--suspend', type=str, required=False,
                             help='Specify whether the user should be suspended.',
                             metavar='False', dest='suspend')


user_rm_parser.add_argument('-u', '--uid', type=str, required=True,
                             help='The user ID to be removed.',
                             metavar='johnny', dest='uid')
user_rm_parser.add_argument('-p', '--purge-data', type=str, required=False,
                             help='When specified the buckets and objects belonging to the user will also be removed.',
                             metavar='True', dest='purge')




key_add_parser.add_argument('-u', '--uid', type=str, required=True,
                             help='The user ID to receive the new key.',
                             metavar='johnny', dest='uid')
key_add_parser.add_argument('-a', '--access-key', type=str, required=False,
                             help='Specify the access key.',
                             metavar='ABCD0EF12GHIJ2K34LMN', dest='access_key')
key_add_parser.add_argument('-s', '--secret-key', type=str, required=False,
                             help='Specify the secret key.',
                             metavar='0AbCDEFg1h2i34JklM5nop6QrSTUV+WxyzaBC7D8',
                             dest='secret_key')
key_add_parser.add_argument('-g', '--generate-key', type=str, required=False,
                             help='Generate a new key pair and add to the existing keyring.',
                             metavar='True', dest='gen_key')

key_rm_parser.add_argument('-a', '--access-key', type=str, required=True,
                             help='The S3 access key belonging to the S3 key pair to remove.',
                             metavar='ABCD0EF12GHIJ2K34LMN', dest='access_key')
key_rm_parser.add_argument('-u', '--uid', type=str, required=False,
                             help='The user to remove the key from.',
                             metavar='johnny', dest='uid')




caps_add_parser.add_argument('-u', '--uid', type=str, required=True,
                             help='The user ID to add an administrative capability to.',
                             metavar='johnny', dest='uid')
caps_add_parser.add_argument('-c', '--caps', type=str, required=False,
                             help='The administrative capability to add to the user.',
                             metavar='"[users|buckets|metadata|usage|zone]=[*|read|write|read, write]"',
                             dest='caps')

caps_rm_parser.add_argument('-u', '--uid', type=str, required=True,
                             help='The user ID to remove an administrative capability from.',
                             metavar='johnny', dest='uid')
caps_rm_parser.add_argument('-c', '--caps', type=str, required=False,
                             help='The administrative capabilities to remove from the user.',
                             metavar='"[users|buckets|metadata|usage|zone]=[*|read|write|read, write]"',
                             dest='caps')
# try:
#     args = parser.parse_args()
#     args.func(args)
#     print args
# except:
#     parser.print_usage()
#     parser.print_help()
#     parser.format_usage()
#     parser.format_help()

args = parser.parse_args()
args.func(args)
print args


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
