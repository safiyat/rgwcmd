from user import User

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
