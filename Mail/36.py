import urllib.request
import json
url = input("Enter json URL: ")
connection = urllib.request.urlopen(url)
data = connection.read()
parsed_data = json.loads(data)
counts = []
comments = parsed_data["comments"]
for comment in comments:
    counts.append(comment['count'])
print("Sum: {0}".format(sum(counts)))
