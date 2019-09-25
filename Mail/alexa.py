import json
import requests
import speech

def lambda_handler(event,context):
   intent_name = event['request']['intent']['name']
   l=[]
   if intent_name == 'news':
           #print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
       m=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=abdb9cdab7e449beb59a53d98319e71d')
       #print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
       data=m.json()
       for i in range(0,len(data['articles'])):
           p=data['articles'][i]['title']
          # print(p)
           #print(type(p))
           l.append(p)
       print(l)
       return speech.speek(str(l))
   else:
       return speech.speek('intent is not correct')