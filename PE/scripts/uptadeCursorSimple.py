#Simple search and replace script
import arcpy
# Retrieve input parameters: the feature class, the field affected by
# the search and replace, the search term, and the replace term.
#fc = r'D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\PE\Lesson3\Alabama.gdb\StateBoundary'

#affectedField = "BOUND_P_"
#oldValue = 1421
#newValue = 1422

fc = arcpy.GetParameterAsText(0)
affectedField = arcpy.GetParameterAsText(1)
oldValue = arcpy.GetParameterAsText(2)
newValue = arcpy.GetParameterAsText(3)
 
# Create the SQL expression for the update cursor. Here this is
#  done on a separate line for readability.
if type(oldValue)=="str":
    queryString = '"' + affectedField + '" = ' + "'" + oldValue + "'"
else:    
#queryString = '"BOUND_P_" = '+ str(oldValue)
    queryString = '"' + affectedField + '" = ' + str(oldValue)
#
 # Create the update cursor and update each row returned by the SQL expression
#cursor = arcpy.da.UpdateCursor(fc, (affectedField,), queryString)
with arcpy.da.UpdateCursor(fc, (affectedField,), queryString) as cursor:
    for row in cursor:
        row[0] = newValue
        cursor.updateRow(row)
print "All done!"
arcpy.AddMessage("All done!")
