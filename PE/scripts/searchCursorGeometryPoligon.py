import arcpy

# Create cursor to retrieve US States shape
featureClass = r"D:\Seva2\2013-14\2015-2016\ProgramGIS\2018\7\PE\Lesson3\USA.gdb\States"
cursor = arcpy.da.SearchCursor(featureClass, ["SHAPE@"])

for row in cursor:
    # Get the geometry object from the shape field
    print("Number of object in States: {0}".format(row[0].partCount))

    # GetPart returns an array of point objects for each part.
    for island in row[0].getPart():
        print("Vertices in states: {0}".format(island.count))
        for point in island:
            print("X: {0}, Y: {1})".format(point.X, point.Y))
