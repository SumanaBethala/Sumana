import json
import boto3
def lambda_handler(event, context):
   a=[]
   b=[]
   # TODO implement
   ec2 = boto3.resource('ec2')
   #instances = ec2.create_instances(
   # ImageId='ami-0de53d8956e8dcf80',
    #MinCount=1,
    #MaxCount=6,
    #InstanceType='t2.micro')
   instances=ec2.instances.filter(Filters=[{'Name':'instance-state-name','Values':['running']}])
   for ins in instances:
       a.append(ins.id)
   instances1=ec2.instances.filter(Filters=[{'Name':'instance-state-name','Values':['stopped']}])
   for ins in instances1:
       b.append(ins.id)
   print('a'+ str(a) + str(len(a)))
   print('b'+ str(b) + str(len(b)))
   
   if len(a) is 0:
       print('no instances are running ')
   else:
       ec2.instances.filter(InstanceIds=a).stop()
   if len(b) is 0:
       print('no instances are in stop state ')
   else:
       ec2.instances.filter(InstanceIds=b).start()
   return 'hi'
