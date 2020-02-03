#!/usr/bin/python

import boto3

client = boto3.client('ec2')


response = client.run_instances(
	BlockDeviceMappings=[
		{
			'DeviceName' :'/dev/xvda',
			'Ebs' : {
				'DeleteOnTermination' : True,
			},
		},
		],

	ImageId= 'ami-04590e7389a6e577c',
	InstanceType= 't2.micro',
	KeyName= 'ec2-keypair',
	MaxCount = 1,
	MinCount = 1,
	Monitoring={
		'Enabled' : False
	},

SecurityGroupIds=['sg-0721330370518f373'],

#SecurityGroups = ['cloud_test1'],

# if you un-comment SecurityGroups , Tags fails because, SecurityGroupId=sg-0721330370518f373 already has SecurityGroup (cloud-test) assigned to it.
SubnetId =  'subnet-1ad6b37d',

TagSpecifications = [
		{

                 		'ResourceType': 'instance',
                 		'Tags': [
                 				{
                 					'Key' : 'Department',
                 					'Value': 'Developers'
                 					},
                 				{
                 					'Key' : 'Name',
                 					'Value' : 'cloud_test'
                 				},
                 				{	
                 					'Key' : 'employee',
                 					'Value' : 'somnath'
                 				},
                 				]

                 				}],


)
   
   
for instance in response['Instances']:
	print(instance['InstanceId'])
	


