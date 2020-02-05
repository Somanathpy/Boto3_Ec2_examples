#!/usr/bin/python
"""
this script displays all existing Security Groups and updates new inbound ip FromPort and ToPort"
"""
import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

response = client.describe_instances()
#print(response)

for r in response["Reservations"]:
	for instance in r["Instances"]:
		id = instance["SecurityGroups"][0]["GroupId"]
		#print(id)
		security_group = ec2.SecurityGroup(id)
		#print(security_group)
                response = security_group.authorize_ingress(IpProtocol = "tcp", CidrIp = "0.0.0.0/0", FromPort = 1234, ToPort = 1234)
