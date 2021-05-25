#add new field in feature class
import arcpy

# Create insert cursor for table
fc = r"D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\PE\Lesson3\USA.gdb\CitiesCopy2"
rows = arcpy.InsertCursor(fc)

# Create 25 new rows. Set the initial row ID and distance values
for x in xrange(1, 26):
    row = rows.newRow()
    row.setValue("UIDENT", x)
    row.setValue("POPCLASS", 1)
    rows.insertRow(row)

# Delete cursor and row objects to remove locks on the data
del row
del rows

print "All done!"
