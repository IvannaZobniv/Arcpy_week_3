#add new field in feature class
import arcpy

fc = r'D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\PE\Lesson3\USA.gdb\CitiesCopy2'
newField = ["NAME","CAPITAL"]

with arcpy.da.InsertCursor(fc, newField) as cursor:       
        cursor.insertRow(["Kiev",3])
        del cursor
print "All done!"
