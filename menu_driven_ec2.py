import boto3
from pprint import pprint
import sys
import os

# This is a sample python script that allows operating on EC2 instances
# Pre requisites:
# 1- Create an IAM user "ec2" and give permissions to:
# -> operate with EC2
# -> programmatic access
# -> policy for EC2 with list, start, stop, terminate
# 2- Run aws configure --profile ec2
# -> enter the keys
# 3- Have some EC2 instances to play around
# 4- Python3 and boto3 installed


#General variables
aws_mag_con=boto3.session.Session(profile_name="ec2")
ec2_con_re=aws_mag_con.resource(service_name="ec2")
ec2_con_cli=aws_mag_con.client(service_name="ec2")
menu = True
msg = ""

#Functions
clear = lambda: os.system('clear') #on Linux System

while menu == True:
    try:
        clear()
        print("This scripts performes the following actions on ec2 instances")
        print("""
    1. start
    2. stop
    3. terminate
    4. exit
            """)
        print("These are your instances:")
        for each_reservation in ec2_con_cli.describe_instances()['Reservations']:
            for each_instance in each_reservation['Instances']:
                pprint("InstanceId: {}".format(each_instance['InstanceId']))
        print(msg)
        opt=int(input("\nEnter your option: "))
        if opt == 1:
            instance_id=input("enter your EC2 instance Id: ")
            my_req_instance_object=ec2_con_re.Instance(instance_id)
            msg = "starting ec2 instance..."
            my_req_instance_object.start()
        elif opt == 2:
            instance_id=input("enter your EC2 instance Id: ")
            my_req_instance_object=ec2_con_re.Instance(instance_id)
            msg = "stopping ec2 instance..."
            my_req_instance_object.stop()
        elif opt == 3:
            instance_id=input("enter your EC2 instance Id: ")
            my_req_instance_object=ec2_con_re.Instance(instance_id)
            msg = "terminating ec2 instance..."
            my_req_instance_object.terminate()
        elif opt == 4:
            print("thanks come back soon...")
            menu = False
        else:
            msg = "invalid option, try again"
    except:
            print("unable to process your request, sorry")
            exit()
