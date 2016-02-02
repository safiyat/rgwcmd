#! /usr/bin/env python
from rgwcmd import commands, rgwconfig, connection, rgwadmin


if __name__ == '__main__':
   #(navneet) Check the config file from rgwconfig
   # Use class to check for params
    conn = rgwadmin.init_connection()

    parser = commands.init_command_parser()
    args = parser.parse_args()
    args.func(args)
