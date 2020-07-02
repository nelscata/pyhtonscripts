"""
This script will look into a ip.txt file for ips that could belong to
EC2 instances public Ip, if the IP is found it will save it in
result.txt
"""

import boto3
aws_con = boto3.session.Session(profile_name="tfgco")

regions = ['us-east-1', 'ap-northeast-1', 'eu-central-1', 'sa-east-1']

ip_found = []


def verify_ip(region):
    print("Looking at " + region)
    ec2_con_cli = aws_con.client(service_name="ec2", region_name=region)
    ip_list = open('ip.txt', 'r')
    for ip in ip_list:
        for ec2_instances in ec2_con_cli.describe_instances(Filters=[{'Name': 'ip-address', 'Values': [ip.rstrip()]}])['Reservations']:
            for instance in ec2_instances['Instances']:
                print ("Found! " + str(instance['PublicIpAddress']))
                ip_found.append(instance['PublicIpAddress'])
    ip_list.close()


for region in regions:
    verify_ip(region)

# Write result to a file
result = open('result.txt', 'w+')
for ip in ip_found:
    result.write(ip+'\n')
result.close()
