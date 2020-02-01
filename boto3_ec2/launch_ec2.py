#!/usr/bin/python

import boto3

client = boto3.client('ec2')
response = client.run_instances(ImageId='ami-04590e7389a6e577c',
					 InstanceType='t2.micro',
					 MinCount=1,
					 MaxCount=1) 
for instance in response['Instances']:
	print(instance['InstanceId'])