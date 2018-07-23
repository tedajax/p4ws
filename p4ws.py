import argparse

# For privacy reasons all the p4 config vars are unset.
# Fill them in with information of your p4 server.

# Location of p4config file.  Should be the same as your P4CONFIG environment variable.
p4config = ''

p4port = ''
p4user = ''
p4ignore = '.p4ignore'
p4host = ''
p4client = ''
p4passwd = ''
p4tickets = ''

parser = argparse.ArgumentParser()
parser.add_argument("client", help="Name of the client to switch to.")
parser.add_argument("-v", "--verbose", help="If true print contents of config file.", action="store_true")
parser.add_argument("-s", "--server", help="If true clear p4host so we can connect to server repo.", action="store_true")

args = parser.parse_args()
p4client = args.client
verbose = args.verbose
server = args.server

print('Switching p4 workspace to ' + args.client + '\n')

with open(p4config, 'w') as config_file:
    config_file.write('P4PORT={}\n'.format(p4port))
    config_file.write('P4USER={}\n'.format(p4user))
    config_file.write('P4IGNORE={}\n'.format(p4ignore))
    if server:
        config_file.write('P4HOST=\n')
    else:
        config_file.write('P4HOST={}\n'.format(p4host))
    config_file.write('P4CLIENT={}\n'.format(p4client))
    config_file.write('P4PASSWD={}\n'.format(p4passwd))
    config_file.write('P4TICKETS={}\n'.format(p4tickets))

with open(p4config, 'r') as config_file:
    print('P4CONFIG file stored at {}:'.format(p4config))
    if verbose:
        print(config_file.read())
