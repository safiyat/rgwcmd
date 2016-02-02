import argparsen as argparse
from argparse import RawTextHelpFormatter as formatter_class
# RawDescriptionHelpFormatter
# RawTextHelpFormatter
# ArgumentDefaultsHelpFormatter
# MetavarTypeHelpFormatter
from rgwadmin import adminutils

command_list = {
    "commands": [
        {

        "user": {
            "subcommands": [
                {

                "create": {
                    "arguments": [
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": str,
                            "required": "True",
                            "help": "The user ID to be created.",
                            "metavar": "johnny",
                            "dest": "uid"
                        }
                        },
                        {
                        "display-name" : {
                            "short": "-d",
                            "long": "--display-name",
                            "type": str,
                            "required": "True",
                            "help": "The display name of the user to be\
                                     created.",
                            "metavar": "Johnny Lever",
                            "dest": "dispname"
                        }
                        },
                        {
                        "email" : {
                            "short": "-e",
                            "long": "--email",
                            "type": str,
                            "required": "False",
                            "help": "The email address associated with the\
                                     user.",
                            "metavar": "johnny.lever@example.com",
                            "dest": "email"
                        }
                        },
                        {
                        "access-key" : {
                            "short": "-a",
                            "long": "--access-key",
                            "type": str,
                            "required": "False",
                            "help": "Specify access key.",
                            "metavar": "ABCD0EF12GHIJ2K34LMN",
                            "dest": "access_key"
                        }
                        },
                        {
                        "secret-key" : {
                            "short": "-s",
                            "long": "--secret-key",
                            "type": str,
                            "required": "False",
                            "help": "Specify secret key.",
                            "metavar": "0AbCDEFg1h2i34JklM5nop6QrSTUV+\
                                        WxyzaBC7D8",
                            "dest": "secret_key"
                        }
                        },
                        {
                        "generate-key" : {
                            "short": "-g",
                            "long": "--generate-key",
                            "type": str,
                            "required": "False",
                            "help": "Generate a new key pair and add to the\
                                     existing keyring.",
                            "metavar": "True",
                            "dest": "gen_key"
                        }
                        },
                        {
                        "caps" : {
                            "short": "-c",
                            "long": "--caps",
                            "type": str,
                            "required": "False",
                            "help": "User capabilities.",
                            "metavar": "\"[users|buckets|metadata|usage|zone]=[*|read|write|read, write]\"",
                            "dest": "caps"
                        }
                        },
                        {
                        "max-buckets" : {
                            "short": "-m",
                            "long": "--max-buckets",
                            "type": str,
                            "required": "False",
                            "help": "Specify the maximum number of buckets\
                                     the user can own.",
                            "metavar": "500",
                            "dest": "max_buckets"
                        }
                        },
                        {
                        "suspend" : {
                            "short": "-x",
                            "long": "--suspend",
                            "type": str,
                            "required": "False",
                            "help": "Specify whether the user should be\
                             suspended.",
                            "metavar": "False",
                            "dest": "suspend"
                        }
                        }
                    ],
                    "function" : adminutils.create_user
                }
                },
                {

                "update": {
                    "arguments": [
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": str,
                            "required": "True",
                            "help": "The user ID to be created.",
                            "metavar": "johnny",
                            "dest": "uid"
                        }
                        },
                        {
                        "display-name" : {
                            "short": "-d",
                            "long": "--display-name",
                            "type": str,
                            "required": "False",
                            "help": "The display name of the user to be\
                                     created.",
                            "metavar": "Johnny Lever",
                            "dest": "dispname"
                        }
                        },
                        {
                        "email" : {
                            "short": "-e",
                            "long": "--email",
                            "type": str,
                            "required": "False",
                            "help": "The email address associated with the\
                                     user.",
                            "metavar": "johnny.lever@example.com",
                            "dest": "email"
                        }
                        },
                        {
                        "access-key" : {
                            "short": "-a",
                            "long": "--access-key",
                            "type": str,
                            "required": "False",
                            "help": "Specify access key.",
                            "metavar": "ABCD0EF12GHIJ2K34LMN",
                            "dest": "access_key"
                        }
                        },
                        {
                        "secret-key" : {
                            "short": "-s",
                            "long": "--secret-key",
                            "type": str,
                            "required": "False",
                            "help": "Specify secret key.",
                            "metavar": "0AbCDEFg1h2i34JklM5nop6QrSTUV+\
                                        WxyzaBC7D8",
                            "dest": "secret_key"
                        }
                        },
                        {
                        "generate-key" : {
                            "short": "-g",
                            "long": "--generate-key",
                            "type": str,
                            "required": "False",
                            "help": "Generate a new key pair and add to the\
                                     existing keyring.",
                            "metavar": "True",
                            "dest": "gen_key"
                        }
                        },
                        {
                        "caps" : {
                            "short": "-c",
                            "long": "--caps",
                            "type": str,
                            "required": "False",
                            "help": "User capabilities.",
                            "metavar": "\"[users|buckets|metadata|usage|zone]=[*|read|write|read, write]\"",
                            "dest": "caps"
                        }
                        },
                        {
                        "max-buckets" : {
                            "short": "-m",
                            "long": "--max-buckets",
                            "type": str,
                            "required": "False",
                            "help": "Specify the maximum number of buckets\
                                     the user can own.",
                            "metavar": "500",
                            "dest": "max_buckets"
                        }
                        },
                        {
                        "suspend" : {
                            "short": "-x",
                            "long": "--suspend",
                            "type": str,
                            "required": "False",
                            "help": "Specify whether the user should be\
                             suspended.",
                            "metavar": "False",
                            "dest": "suspend"
                        }
                        }
                    ],
                    "function" : adminutils.update_user
                }
                },
                {

                "rm": {
                    "arguments": [
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": str,
                            "required": "True",
                            "help": "The user ID to be created.",
                            "metavar": "johnny",
                            "dest": "uid"
                        }
                        },
                        {
                        "purge-data" : {
                            "short": "-p",
                            "long": "--purge-data",
                            "type": str,
                            "required": "False",
                            "help": "When specified the buckets and objects\
                                     belonging to the user will also be\
                                     removed.",
                            "metavar": "True",
                            "dest": "purge"
                        }
                        }
                    ],
                    "function" : adminutils.remove_user
                }
                },
                {

                "info": {
                    "arguments": [
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": str,
                            "required": "True",
                            "help": "The user ID to be created.",
                            "metavar": "johnny",
                            "dest": "uid"
                        }
                        }
                    ],
                    "function" : adminutils.update_user
                }
                }

             ],
            "dest": "subcommand"
        }
        },
        {

        "keys": {
            "subcommands": [
                {

                "add": {
                    "arguments": [
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": str,
                            "required": "True",
                            "help": "The user ID to receive the new key.",
                            "metavar": "johnny",
                            "dest": "uid"
                        }
                        },
                        {
                        "access-key" : {
                            "short": "-a",
                            "long": "--access-key",
                            "type": str,
                            "required": "False",
                            "help": "Specify access key.",
                            "metavar": "ABCD0EF12GHIJ2K34LMN",
                            "dest": "access_key"
                        }
                        },
                        {
                        "secret-key" : {
                            "short": "-s",
                            "long": "--secret-key",
                            "type": str,
                            "required": "False",
                            "help": "Specify secret key.",
                            "metavar": "0AbCDEFg1h2i34JklM5nop6QrSTUV+\
                                        WxyzaBC7D8",
                            "dest": "secret_key"
                        }
                        },
                        {
                        "generate-key" : {
                            "short": "-g",
                            "long": "--generate-key",
                            "type": str,
                            "required": "False",
                            "help": "Generate a new key pair and add to the\
                                     existing keyring.",
                            "metavar": "True",
                            "dest": "gen_key"
                        }
                        }
                    ],
                    "function" : adminutils.add_key
                }
                },
                {

                "rm": {
                    "arguments": [
                        {
                        "access-key" : {
                            "short": "-a",
                            "long": "--access-key",
                            "type": str,
                            "required": "True",
                            "help": "Specify access key.",
                            "metavar": "ABCD0EF12GHIJ2K34LMN",
                            "dest": "access_key"
                        }
                        },
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": str,
                            "required": "False",
                            "help": "The user ID to remove the key from.",
                            "metavar": "johnny",
                            "dest": "uid"
                        }
                        }
                    ],
                    "function" : adminutils.remove_key
                }
                }
            ],
            "dest": "subcommand"
        }
        },
        {

        "caps": {
            "subcommands": [
                {

                "add": {
                    "arguments": [
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": str,
                            "required": "True",
                            "help": "The user ID to add the capabilities\
                                     to.",
                            "metavar": "johnny",
                            "dest": "uid"
                        }
                        },
                        {
                        "caps" : {
                            "short": "-c",
                            "long": "--caps",
                            "type": str,
                            "required": "True",
                            "help": "User capabilities.",
                            "metavar": "\"[users|buckets|metadata|usage|zone]=[*|read|write|read, write]\"",
                            "dest": "caps"
                        }
                        }
                    ],
                    "function" : adminutils.add_caps
                }
                },
                {

                "rm": {
                    "arguments": [
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": str,
                            "required": "False",
                            "help": "The user ID to remove the capabilities\
                                     from.",
                            "metavar": "johnny",
                            "dest": "uid"
                        }
                        },
                        {
                        "caps" : {
                            "short": "-c",
                            "long": "--caps",
                            "type": str,
                            "required": "True",
                            "help": "User capabilities.",
                            "metavar": "\"[users|buckets|metadata|usage|zone]=[*|read|write|read, write]\"",
                            "dest": "caps"
                        }
                        }
                    ],
                    "function" : adminutils.remove_caps
                }
                }
            ],
            "dest": "subcommand"
        }
        }
    ],
    "dest": "command"
}

def init_command_parser():
    parser = argparse.ArgumentParser(
        # description = 'Ceph Rados Gateway REST API on the cmd.',
        # formatter_class=formatter_class)
        description = 'Ceph Rados Gateway REST API on the cmd.')
    #(navneet) add formatter class to all parsers in subparsers.
    base_subparsers = parser.add_subparsers(dest="command")

    # Iterates over user, keys, caps
    for command in command_list['commands']:
        # command_parser = base_subparsers.add_parser(command.keys()[0],
        #                     formatter_class=formatter_class)
        command_parser = base_subparsers.add_parser(command.keys()[0])
        # Iterates over subcommands, function and dest
        for key, value in command.iteritems():
            subparsers = command_parser.add_subparsers(dest=value['dest'])
            # Iterates over create, update, rm, info; etc
            for command in value['subcommands']:
                # command_parser = subparsers.add_parser(command.keys()[0],
                #                                  formatter_class=formatter_class)
                command_parser = subparsers.add_parser(command.keys()[0])
                # Iterates over a single entry in the dictionary:arguments
                for command, properties  in command.iteritems():
                    # Iterates over arguments to a single command: uid, email...
                    command_parser.set_defaults(func=properties['function'])
                    for argument in properties['arguments']:
                        # Iterates over kv pairs in arguments:short,long,type...
                        for key, value in argument.iteritems():
                            # print value['dest']
                            command_parser.add_argument(value['short'],
                                                        value['long'],
                                                        type=value['type'],
                                                        required=
                                                        value['required'],
                                                        help=value['help'],
                                                        metavar=
                                                        value['metavar'],
                                                        dest=value['dest'])
    return parser
