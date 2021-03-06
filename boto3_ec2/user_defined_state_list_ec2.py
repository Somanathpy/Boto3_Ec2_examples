#!/usr/bin/python
#access_key and secret key and default-region=us-west-2 has been configured in ~/.aws/config and ~/.aws/credentials

import boto3
import sys

ec2 = boto3.resource('ec2')

state = sys.argv[1]
print(state)

for instance in ec2.instances.all():
    if instance.state['Name'] == state:
         print("Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state))
            
