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

args = parser.parse_args()
p4client = args.client

print('Switching p4 workspace to ' + args.client + '\n')

with open(p4config, 'w') as config_file:
    config_file.write('P4PORT={}\n'.format(p4port))
    config_file.write('P4USER={}\n'.format(p4user))
    config_file.write('P4IGNORE={}\n'.format(p4ignore))
    config_file.write('P4HOST={}\n'.format(p4host))
    config_file.write('P4CLIENT={}\n'.format(p4client))
    config_file.write('P4PASSWD={}\n'.format(p4passwd))
    config_file.write('P4TICKETS={}\n'.format(p4tickets))

with open(p4config, 'r') as config_file:
    print('P4CONFIG file stored at {}:'.format(p4config))
    print(config_file.read())
