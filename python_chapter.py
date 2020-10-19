import urllib.request as ur
import xml.etree.ElementTree as et

sum = 0

url = input('Enter URL: ')
#http://py4e-data.dr-chuck.net/comments_998849.xml
print('Retrieving', url)

xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

#form tree
tree = et.fromstring(xml)
counts = tree.findall('.//count')

for count in counts:
    sum += int(count.text)

print(sum)