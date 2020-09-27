import http.client
import urllib.request
import requests
import json



URL = 'https://api.thingspeak.com/channels/1161297/feeds.json?api_key='
KEY = 'LDVBHGXFKH4LFUQW'
HEADER = '&results=5'
NEW_URL = URL+KEY+HEADER
#print(NEW_URL)

get_data = requests.get(NEW_URL).json()
channel_id = get_data['channel']['id']

field_1 = get_data['feeds']

t=[]

for x in field_1:
    t.append(x['field1'])
    
print("Latest 5 readings for temperature:\n")
print(t)

