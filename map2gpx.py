#!/usr/bin/python3

import sys
import csv

if len(sys.argv) != 2:
    print("*.map filename required")
    sys.exit(1)

map_file_name = sys.argv[1]

print("""<?xml version="1.0" encoding="UTF-8" ?>
<gpx xmlns="http://www.topografix.com/GPX/1/1" version="1.1" creator="map2gpx - https://github.com/Geremia/map2gpx" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd ">
	<trk>
		<name><![CDATA[""" + map_file_name + """]]> </name>
		<trkseg>""")

with open(map_file_name, newline='') as csvfile:
    data = list(csv.reader(csvfile))

#['A', '061120', '092833', '3322.2928', 'N', '11204.7423', 'W', '000.00', '0.00', '0.00', '0.00;']

for i in data:
    date_str = i[1]
    time = i[2]

    latsign = lonsign = ''
    if i[4] == 'S':
        latsign = '-'
    if i[6] == 'W':
        lonsign = '-'
    lat = str(round(float(latsign + i[3])/100.,6))
    lon = str(round(float(lonsign + i[5])/100.,6))
    year = '20' + date_str[4:6]
    month = date_str[2:4]
    day = date_str[0:2]
    hour = time[0:2]
    minute = time[2:4]
    second = time[4:6]

    print("			<trkpt lat=\"" + lat + "\" lon=\"" + lon + "\">")
    print("				<time>" + year + '-' + month + '-' + day + 'T' + hour + ':' + minute + ':' + second + 'Z</time>')
    print("			</trkpt>")

print("""		</trkseg>
	</trk>
</gpx>""")
