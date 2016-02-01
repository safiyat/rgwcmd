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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
                            "required": "False",
                            "help": "Specify whether the user should be\
                             suspended.",
                            "metavar": "False",
                            "dest": "suspend"
                        }
                        }
                    ]
                }
                },
                {

                "update": {
                    "arguments": [
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
                            "required": "False",
                            "help": "Specify whether the user should be\
                             suspended.",
                            "metavar": "False",
                            "dest": "suspend"
                        }
                        }
                    ]
                }
                },
                {

                "rm": {
                    "arguments": [
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": "str",
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
                            "type": "str",
                            "required": "False",
                            "help": "When specified the buckets and objects\
                                     belonging to the user will also be\
                                     removed.",
                            "metavar": "True",
                            "dest": "purge"
                        }
                        }
                    ]
                }
                },
                {

                "info": {
                    "arguments": [
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": "str",
                            "required": "True",
                            "help": "The user ID to be created.",
                            "metavar": "johnny",
                            "dest": "uid"
                        }
                        }
                    ]
                }
                }

             ],
            "function" : "user_func",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
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
                            "type": "str",
                            "required": "False",
                            "help": "Generate a new key pair and add to the\
                                     existing keyring.",
                            "metavar": "True",
                            "dest": "gen_key"
                        }
                        }
                    ]
                }
                },
                {

                "rm": {
                    "arguments": [
                        {
                        "access-key" : {
                            "short": "-a",
                            "long": "--access-key",
                            "type": "str",
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
                            "type": "str",
                            "required": "False",
                            "help": "The user ID to remove the key from.",
                            "metavar": "johnny",
                            "dest": "uid"
                        }
                        }
                    ]
                }
                }
            ],
            "function" : "keys_func",
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
                            "type": "str",
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
                            "type": "str",
                            "required": "True",
                            "help": "User capabilities.",
                            "metavar": "\"[users|buckets|metadata|usage|zone]=[*|read|write|read, write]\"",
                            "dest": "caps"
                        }
                        }
                    ]
                }
                },
                {

                "rm": {
                    "arguments": [
                        {
                        "uid" : {
                            "short": "-u",
                            "long": "--uid",
                            "type": "str",
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
                            "type": "str",
                            "required": "True",
                            "help": "User capabilities.",
                            "metavar": "\"[users|buckets|metadata|usage|zone]=[*|read|write|read, write]\"",
                            "dest": "caps"
                        }
                        }
                    ]
                }
                }
            ],
            "function" : "caps_func",
            "dest": "subcommand"
        }
        }
    ],
    "dest": "command"
}
