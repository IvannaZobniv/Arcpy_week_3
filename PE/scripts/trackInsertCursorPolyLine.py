# This script reads a GPS track in CSV format and writes geometries from the list of coordinate pairs
import csv
import arcpy
import os
# Set up input and output variables for the script
gpsTrack = open(r"D:\Seva2\2013-14\2015-2016\ProgramGIS\2018\7\PE\Lesson3\gps_track.txt")
polylineFC = r"D:\Seva2\2013-14\2015-2016\ProgramGIS\2018\7\PE\Lesson3\tracklines.shp"
if not os.path.isfile(polylineFC):
    from arcpy import env
    env.workspace = r"D:\Seva2\2013-14\2015-2016\ProgramGIS\2018\7\PE\Lesson3"
    arcpy.CreateFeatureclass_management(env.workspace, "tracklines.shp", "POLYLINE", "", "DISABLED", "DISABLED", r"D:\Seva2\2013-14\2015-2016\ProgramGIS\2018\7\PE\Lesson3\counties.shp")
spatialRef = arcpy.Describe(polylineFC).spatialReference
# Set up CSV reader and process the header
csvReader = csv.reader(gpsTrack)
header = csvReader.next()
latIndex = header.index("lat")
lonIndex = header.index("long")
# Create an empty array object
vertexArray = arcpy.Array()
# Loop through the lines in the file and get each coordinate
for row in csvReader:
    lat = float(row[latIndex])
    lon = float(row[lonIndex]) 
    # Make a point from the coordinate and add it to the array
    vertex = arcpy.Point(lon,lat)
    vertexArray.add(vertex)
# Write the array to the feature class as a polyline feature
with arcpy.da.InsertCursor(polylineFC, ("SHAPE@",)) as cursor:
    polyline = arcpy.Polyline(vertexArray, spatialRef)
    cursor.insertRow((polyline,))
print "All done!"
