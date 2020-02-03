#!/usr/bin/python

import boto3
import pprint

ec2 = boto3.client('ec2')

response = ec2.describe_instances()
pprint.pprint(response)
