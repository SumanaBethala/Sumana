import json
def lambda_handler(event, context):
   print(event)
   try:
       sum=event['a']+event['b']
       print(sum)
       return sum
   except:
       return('error')