# # Insert the geometry of point in the cities
import arcpy
arcpy.env.workspace = r"D:\Seva2\2013-14\2015-2016\ProgramGIS\2018\7\PE\Lesson3\USA.gdb"
featureClassList = arcpy.ListFeatureClasses()
featureClass = "Temp"
if featureClass not in featureClassList:    
    arcpy.CreateFeatureclass_management(arcpy.env.workspace, featureClass, "POINT", "Cities", "DISABLED", "DISABLED", "Cities")
    print "Temp was created"
insertedField = ["SHAPE@XY"]
# Define array for points
xy = ((-97.7624204537, 28.3709213515),
      (-80.1164167102, 26.3299831143),
      (-81.8008128002, 26.6600164123),
      (-80.1358864047, 26.1503917519),
      (-80.3203965408, 25.9088593326),
      (-81.7737622983, 26.1454599642),
      (-80.2244915167, 25.7804603874),
      (-97.4270261477, 27.757033849))
# Loop through each row and insert all geometry for it
with arcpy.da.InsertCursor(featureClass,insertedField) as cursor:
    for row in xy:
        cursor.insertRow([row])
print "All done!"

