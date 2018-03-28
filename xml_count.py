import urllib.error
import xml.etree.ElementTree as ET

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
sample_data = 'http://py4e-data.dr-chuck.net/comments_42.xml'
actual_data = 'http://py4e-data.dr-chuck.net/comments_81418.xml'
sum = 0
counts_array=[]

while True:
	
	open_url = urllib.request.urlopen(actual_data)
	data = open_url.read()
	tree = ET.fromstring(data)
	
	counts = tree.findall('.//count')
	
	# print(counts)
	# index = input('type to continue')
	for items in counts:
		sum = sum + int(items.text)
		
	print('final sum %d' %sum)
	break
