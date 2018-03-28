import json
import urllib.request, urllib.parse, urllib.error

sample_data = 'http://py4e-data.dr-chuck.net/comments_42' # (Sum=2553)
actual_data = 'http://py4e-data.dr-chuck.net/comments_81419.json' # (Sum ends with 35)

while True:
	
	sum = 0
	data = input('Type in the url or hit enter for default: ')
	
	if len(data)<1:
		data = actual_data
	
	url = urllib.request.urlopen(data)
	data = url.read()
	data = data.decode('UTF-8')
	json_items = json.loads(data)
	# print(json_items['comments'])
	index = 0
	
	for items in json_items['comments']:
		
		sum = sum + int(json_items['comments'][index]['count'])
		index = index + 1
	
	
	print(sum)
	break