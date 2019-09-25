import urllib.request
import json
import ssl
url='https://newsapi.org/v2/everything?q=bitcoin&from=2019-03-23&sortBy=publishedAt&apiKey=4d0ae83c86f14fc386bae7deb97f79f8'
gcontext=ssl.SSLContext()
data=urllib.request.urlopen(url,context=gcontext).read()
json_data=data.decode()
print(type(json_data))
x=json.loads(json_data)
print(x)