import http.client
import urllib.parse
import time
key = "AT68QYQ94MQEWXL3" # Put your API Key here
params = urllib.parse.urlencode({'group': 'L3-T-5', 'cmail': 'colinmckay@cmail.carleton.ca', 'memberID': 'd', 'key':key })
headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("api.thingspeak.com:80")
try:
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    conn.close()
except:
    print("connection failed")

