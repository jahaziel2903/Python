import urllib.request as ur
import xml.etree.ElementTree as et
import json

sum = 0



url = input('Enter URL: ')
#http://py4e-data.dr-chuck.net/comments_998849.xml
print('Retrieving', url)

data = ur.urlopen(url).read().decode()
info = json.loads(data)

print('Retrieved', len(info), 'characters')


for item in info['comments']:
    sum += int(item['count'])

print(sum)
