import sqlite3
import json

# Connect to the SQLite database
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# Open the output file in write mode
with open('where.js', 'w', encoding="utf-8") as fhand:
    fhand.write("myData = [\n")
    count = 0

    # Retrieve data from the database
    cur.execute('SELECT geodata FROM Locations')
    for row in cur:
        data = row[0]
        try:
            js = json.loads(data)
        except json.JSONDecodeError as e:
            print("JSON decode error:", e)
            continue

        if not ('status' in js and js['status'] == 'OK'):
            continue

        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        if lat == 0 or lng == 0:
            continue
        where = js['results'][0]['formatted_address']
        where = where.replace("'", "")

        try:
            print(where, lat, lng)
            count = count + 1

            if count > 1:
                fhand.write(",\n")

            output = "[" + str(lat) + "," + str(lng) + ", '" + where + "']"
            fhand.write(output)
        except Exception as e:
            print("Error:", e)
            continue

    fhand.write("\n];\n")

# Close the database connection
conn.close()

print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
