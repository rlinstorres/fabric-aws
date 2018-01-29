# -*- coding: UTF-8 -*-

from fabric.api import run, env, hosts
from boto import ec2
from collections import defaultdict
import os

# Server user, normally AWS Ubuntu instances have default user "ubuntu"
env.user = "ubuntu"

# List of AWS private key Files
env.key_filename = ["~/.ssh/key-name.pem"]

# Export Access_Key and Secret_key
access_key = os.environ.get("ACCESS_KEY")
secret_key = os.environ.get("SECRET_KEY")

print 'connecting to aws and listing instances'
conn = ec2.connect_to_region(region_name='us-east-1', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
instances = [i for r in conn.get_all_instances() for i in r.instances if i.private_ip_address]

class AWSDict(dict):

    def __contains__(self, key):
        return True

    def __missing__(self, key):
        self[key] = [i.private_ip_address for i in instances if 'Name' in i.tags and i.tags['Name'] == key]
        return self[key]

env.roledefs = AWSDict()
env.roledefs['all'] = [i.private_ip_address for i in instances]

###########
## Tasks ##
###########

# Exemplo 1
def exec_exemplo_1():
    run('sudo service nginx restart')

# Exemplo 2
def exec_exemplo_2():
    run('sudo hostname')
