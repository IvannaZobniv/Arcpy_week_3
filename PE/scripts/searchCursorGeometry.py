# Finds the geometry of point in the cities
 
import arcpy
 
featureClass = r"D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\PE\Lesson3\USA.gdb\CitiesCopy2"
searchedField = ["OID@","SHAPE@XY"]
 
# Loop through each row and keep all geometry for it
 
with arcpy.da.SearchCursor(featureClass, searchedField) as cursor:
    for row in cursor:
        print "{0} : X={1} Y={2}".format(row[0],row[1][0],row[1][1])
    print "Coodrinate system: " + arcpy.Describe(featureClass).spatialReference.name
    print "Datum name: " + arcpy.Describe(featureClass).spatialReference.datumName
