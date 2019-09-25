import xml.etree.ElementTree as ET
from urllib.request import urlopen
url = input()
xml = urlopen(url).read()
stuff = ET.fromstring(xml)
lst = stuff.findall('comments/comment')
print("count comment:", len(lst))
sum_val = 0
for item in lst:
    val = int(item.find("count").text)
    sum_val += val
print(sum_val)
