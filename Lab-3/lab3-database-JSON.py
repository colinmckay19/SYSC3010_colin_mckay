from urllib.request import * 
from urllib.parse import * 
import json
import sqlite3


# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa


# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7"

# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
  # results is a JSON string
webData.close()

print (results)
#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

city = data["name"]
pressure = data["main"]["pressure"]

dbconnect = sqlite3.connect("mydatabase.db")
dbconnect.row_factory = sqlite3.Row
cursor = dbconnect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS cityPressure (city text, pressure integer);''')
cursor.execute('''INSERT INTO cityPressure values (?, ?)''', (city, pressure))

dbconnect.commit();

cursor.execute('SELECT * FROM cityPressure')
print("\n")
for row in cursor:
    print(row['city'],row['pressure'])

dbconnect.close();

