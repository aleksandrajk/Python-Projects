import urllib.request
import sqlite3
import json
import time

# Replace 'YOUR_API_KEY' with your actual Google Maps Geocoding API key
api_key = 'YOUR_API_KEY'

serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

scontext = None

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

fh = open("where.data")
count = 0
for line in fh:
    if count > 200:
        break
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (memoryview(address.encode()),))

    try:
        data = cur.fetchone()[0]
        print("Found in database ", address)
        continue
    except:
        pass

    print('Resolving', address)
    url = serviceurl + urllib.parse.urlencode({"sensor": "false", "address": address, "key": api_key})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=scontext)
    data = uh.read()
    data = data.decode('utf-8')  # Decode data to str before performing string operations
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1
    try:
        js = json.loads(data)
        # print js  # We print in case unicode causes an error
    except:
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()
    time.sleep(1)

print("Run geodump.py to read the data from the database so you can visualize it on a map.")
