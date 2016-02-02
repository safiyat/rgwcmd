#! /usr/bin/env python

from rgwcmd import argparsen
from rgwcmd.rgwadmin import adminutils


# load argument parser here

if __name__ == '__main__':

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

if __name__ == '__main__':
   # Check the config file from rgwconfig
   # Use class to check for params
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
