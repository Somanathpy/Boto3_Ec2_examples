import boto3

ec2 = boto3.resource('ec2')

running_instances = []

#adding running instances to a list

for instance in ec2.instances.all():
	if instance.state['Name'] == 'running':
		running_instances.append(instance.id)

print(" Currently running instances are ...")
for id in running_instances:
	print(id)
	instance = ec2.Instance(id)
	response = instance.terminate()
	print(response)
