import boto3
ec2 = boto3.resource('ec2')

# create an instance
ec2.create_instances(ImageId='ami-00068cd7555f543d5', MinCount=1, MaxCount=1)

# terminate an instance
ids = ['i-04d55ec0552e0bb40']
ec2.instances.filter(InstanceIds=ids).terminate()
print('done')
