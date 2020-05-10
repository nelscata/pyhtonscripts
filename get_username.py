import boto3
import sys
aws_mag_con=boto3.session.Session(profile_name="default")
iam_con_re=aws_mag_con.resource(service_name="iam")

#Given a user Id returns the User Name
try:
  for user in iam_con_re.users.all():
    if user.user_id == sys.argv[1]:
      print("UserName: " + user.name + ", UserId: " + user.user_id)
except:
  print("Error processing your request")
