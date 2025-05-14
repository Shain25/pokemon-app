import boto3
import os

ec2=boto3.client('ec2', region_name='us-west-2')

key_name='pokemon-key'
key_pair=ec2.create_key_pair(KeyName=key_name)
with open(f'{key_name}.pem', 'w') as file:
    file.write(key_pair['KeyMaterial'])
os.chmod(f'{key_name}.pem', 0o400)


sec_group_name='pokemon-sg'
sec_group=ec2.create_security_group(
        GroupName=sec_group_name,
        Description='Allow SSH and HTTP')

sg_id=sec_group['GroupId']

ec2.authorize_security_group_ingress(
        GroupId=sg_id, IpPermissions=[
            {
                'IpProtocol':'tcp',
                'FromPort':22,
                'ToPort':22,
                'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
                },
            {
                'IpProtocol':'tcp',
                'FromPort':80,
                'ToPort':80,
                'IpRanges':[{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )

user_data_script='''#!/bin/bash
exec > /var/log/user-data.log 2>&1
set -x

yum update -y
yum install -y git python3

cd /home/ec2-user
git clone https://github.com/Shain25/pokemon-app.git
cd pokemon-app
chmod 777 pokemons.json
echo 'cd ~/pokemon-app' >> /home/ec2-user/.bashrc
echo 'echo "Welcome! To run the app, type: python3 main.py"' >> /home/ec2-user/.bashrc
chown ec2-user:ec2-user /home/ec2-user/.bashrc
'''

instance=ec2.run_instances(
        ImageId='ami-07b0c09aab6e66ee9',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName=key_name,
        SecurityGroupIds=[sg_id],
        UserData=user_data_script
        )


instance_id=instance['Instances'][0]['InstanceId']
print(f"Instance {instance_id} created, waiting for it to be ready...")

ec2_resource=boto3.resource('ec2')
instance_obj=ec2_resource.Instance(instance_id)
instance_obj.wait_until_running()
instance_obj.reload()

print(f"Instance is ready! Public IP: {instance_obj.public_ip_address}")
