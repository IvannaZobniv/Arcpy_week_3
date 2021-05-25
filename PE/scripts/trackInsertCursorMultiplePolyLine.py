# This script reads a GPS track in CSV format and
#  writes geometries from the list of coordinate pairs
#  Handles multiple polylines
 
# Function to add a polyline
def addPolyline(cursor, array, sr):
    polyline = arcpy.Polyline(array, sr)
    cursor.insertRow((polyline,))
    array.removeAll()
 
# Main script body
import csv
import arcpy
import os
 
# Set up input and output variables for the script
gpsTrack = open(r"D:\Seva2\2013-14\2015-2016\ProgramGIS\2018\7\PE\Lesson3\gps_track_multiple.txt", "r")
polylineFC = r"D:\Seva2\2013-14\2015-2016\ProgramGIS\2018\7\PE\Lesson3\tracklines_sept25.shp"
if not os.path.isfile(polylineFC):
    from arcpy import env
    env.workspace = r"D:\Seva2\2013-14\2015-2016\ProgramGIS\2018\7\PE\Lesson3"
    arcpy.CreateFeatureclass_management(env.workspace, "tracklines_sept25.shp", "POLYLINE", "", "DISABLED", "DISABLED", r"D:\Seva2\2013-14\2015-2016\ProgramGIS\2018\7\PE\Lesson3\counties.shp")

spatialRef = arcpy.Describe(polylineFC).spatialReference
 
# Set up CSV reader and process the header
csvReader = csv.reader(gpsTrack.read().splitlines())
header = csvReader.next()
latIndex = header.index("lat")
lonIndex = header.index("long")
newIndex = header.index("new_seg")
 
# Write the array to the feature class as a polyline feature
with arcpy.da.InsertCursor(polylineFC, ("SHAPE@",)) as cursor:
 
    # Create an empty array object
    vertexArray = arcpy.Array()
 
    # Loop through the lines in the file and get each coordinate
    for row in csvReader:
         
        isNew = row[newIndex].upper()
 
        # If about to start a new line, add the completed line to the
        #  feature class
        if isNew == "TRUE":
            if vertexArray.count > 0:
                addPolyline(cursor, vertexArray, spatialRef)
 
        # Get the lat/lon values of the current GPS reading
        lat = float(row[latIndex])
        lon = float(row[lonIndex])
 
        # Make a point from the coordinate and add it to the array
        vertex = arcpy.Point(lon,lat)
        vertexArray.add(vertex)
 
    # Add the final polyline to the shapefile
    addPolyline(cursor, vertexArray, spatialRef)

print "All done!"
