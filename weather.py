
import urllib2
import json


#f = urllib2.urlopen('http://api.wunderground.com/api/e2e5d4f1d705983d/geolookup/conditions/zipcode.json')
f = urllib2.urlopen('http://api.wunderground.com/api/e2e5d4f1d705983d/hourly10day/q//us/nc/durham.json')
json_string = f.read()
parsed_json = json.loads(json_string)
f.close()
#print(parsed_json)
for item in parsed_json['english']:
    print("item is" + str(item))
