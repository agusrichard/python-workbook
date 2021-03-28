import argparse

parser = argparse.ArgumentParser(description='Run internal command of the service')
parser.add_argument('main_command',help='Main command' )
parser.add_argument('-email', '--email', help='User email')
parser.add_argument('-password', '--password', help='User password')

args = parser.parse_args()

if args.main_command == 'admin':
    print(args)
elif args.main_command == 'run':
    print('running')