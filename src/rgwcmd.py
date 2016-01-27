import argparse

########################### Pure Genius. Never delete. ####################################
###########################################################################################
# command_list = {
#     "user": {
#         "create": {
#             "foo": []
#         }
#     }
# }
# parser = argparse.ArgumentParser(description='Ceph Rados Gateway REST API on the cmd.')
# subparsers = parser.add_subparsers(dest="command")

# for command, subcommands in command_list.iteritems():
#     command_parser = subparsers.add_parser(command)
#     subcommand_parser = command_parser.add_subparsers(dest="subcommand")
#     for subcommand, arguments in subcommands.iteritems():
#         p = subcommand_parser.add_parser(subcommand)
#         p.set_defaults(func=foo)
#         for argument, helper in arguments.iteritems():
#             p.add_argument(argument)
############################################################################################

# if __name__ == '__main__':

parser = argparse.ArgumentParser(description='Ceph Rados Gateway REST API on the cmd.')
subparsers = parser.add_subparsers()

user_parser = subparsers.add_parser('user')
key_parser = subparsers.add_parser('key')
caps_parser = subparsers.add_parser('caps')

user_subparsers = user_parser.add_subparsers()
key_subparsers = key_parser.add_subparsers()
caps_subparsers = caps_parser.add_subparsers()


user_create_parser = user_subparsers.add_parser('create')
user_update_parser = user_subparsers.add_parser('update')
user_rm_parser = user_subparsers.add_parser('rm')

key_add_parser = key_subparsers.add_parser('add')
key_rm_parser = key_subparsers.add_parser('rm')

caps_add_parser = caps_subparsers.add_parser('add')
caps_rm_parser = caps_subparsers.add_parser('rm')
