# -*- coding: utf-8 -*-

import sys, getopt, os


def get_args(argv):
    args_dict = {'host': '', 'user': '', 'password': '', 'database': 'SisenMESS-User-Database', 'path': ''}
    help_msg = """
    example: mail_list.exe -h 127.0.0.1 -u username -p yourpass -d SisenMESS-User-Database --path="D:\mail_list.csv"
    usage:
        -h, --host  SQLServer address
        -u, --user  username to get access to the database
        -p, --password  password to get access to the database
        -d, --database  database name, default db name: SisenMESS-User-Database
        --path  output csv file full path, default path: current/working/dir/mail_list.csv
    """
    try:
        opts, args = getopt.getopt(argv, '-h:-u:-p:-d:', ['help', 'host=', 'user=', 'password=', 'database=', 'path='])
    except getopt.GetoptError:
        print(help_msg)
        sys.exit(2)
    if opts == []:
        print(help_msg)
        sys.exit()
    for opt, arg in opts:
        if opt == '--help':
            print(help_msg)
            sys.exit()
        elif opt in ('-h', '--host'):
            args_dict['host'] = arg
        elif opt in ('-u', '--user'):
            args_dict['user'] = arg
        elif opt in ('-p', '--password'):
            args_dict['password'] = arg
        elif opt in ('-d', '--database'):
            args_dict['database'] = arg
        elif opt in ('--path',):
            args_dict['path'] = arg

    if args_dict['database'] == '':
        args_dict['database'] = 'SisenMESS-User-Database'
    if args_dict['path'] == '':
        args_dict['path'] = os.path.join(os.getcwd(), 'mail_list.csv')

    for k in args_dict:
        if k != 'path' and args_dict[k] == '':
            print('Incomplete Parameters' + '\n' + 'Parameter:" {0} " is not optional!'.format(
                k) + '\n' + 'Try --help to get help msg.')
            sys.exit()

    return args_dict
