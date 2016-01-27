import argparse

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


parser = argparse.ArgumentParser(description='Ceph Rados Gateway REST API on the cmd.')
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
