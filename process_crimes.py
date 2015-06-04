import simplejson as json
import csv
import datetime

keys = []

def formatDateTime(dateVal, timeVal):
  dtString = dateVal.split(":")[0] + ":" + timeVal
  return datetime.datetime.strptime(dtString, "%Y-%m-%dT%H:%M:%S")

with open("sfcrime.json") as f:
  text = f.read()
  crimes = json.loads(text)
  meta = crimes["meta"]
  data = crimes["data"]

  for column in meta["view"]["columns"]:
    if "tableColumnId" in column.keys():
      name = column["name"]
      columnId = column["tableColumnId"]
      position = column["position"]
      print "%s (%i): position %i" % (name, columnId, position)
      keys.append(name)
  
  rowsWritten = 0
  with open("crimes.csv", "w") as output:
    # write headers
    writer = csv.writer(output)
    # These headers are a hack to make crime data look like earthquake data :P
    writer.writerow(["time","latitude","longitude","depth","mag","magType","nst","gap","dmin","rms","net","id","updated","place","type"])
    for row in data:
      dateVal = row[keys.index("Date") + 8]
      timeVal = row[keys.index("Time") + 8]
      date = formatDateTime(dateVal, timeVal)
      lat = row[keys.index("Y") + 8]
      lon = row[keys.index("X") + 8]
      writer.writerow([
        date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        lat, lon,
        "","5.0","","","","","","","","","",""
      ])
      rowsWritten += 1
      if rowsWritten % 1000 == 0:
        print "%i rows written to csv..." % rowsWritten
