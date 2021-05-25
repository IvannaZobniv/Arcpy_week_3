import arcpy

arcpy.env.overwriteOutput = True
Countries =arcpy.GetParameterAsText(0)#r'D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\Programming_in_GIS_2020_L7_p12\Salvador.gdb\CentralAmerica'
OSMpoints =arcpy.GetParameterAsText(1)#r'D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\Programming_in_GIS_2020_L7_p12\Salvador.gdb\OSMpoints'
amenity = ['school','hospital','place_of_worship']
country = 'El Salvador'
workspace= arcpy.GetParameterAsText(2)#r'D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\Programming_in_GIS_2020_L7_p12'
out_name = arcpy.GetParameterAsText(3)#r'D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\Programming_in_GIS_2020_L7_p12\Salvador.gdb'

arcpy.env.workspace = workspace
print("yes_1")
arcpy.MakeFeatureLayer_management(OSMpoints,'osm')
arcpy.MakeFeatureLayer_management(Countries,'country', '"NAME" =' + "'" + country + "'")

print("yes_2")
arcpy.SelectLayerByLocation_management('osm', 'WITHIN', 'country')
for shel in amenity:
    arcpy.MakeFeatureLayer_management('osm',shel+'1','"amenity"='+"'"+shel+"'")
    arcpy.CopyFeatures_management(shel+'1', out_name + '\\' + str(shel))
    arcpy.AddField_management(out_name + '\\' + str(shel),'source','TEXT')
    arcpy.AddField_management(out_name + '\\' + str(shel),'GID','DOUBLE')
    arcpy.AddMessage('Amenities in'+str(country)+' ' +str(shel) +' type are found')
    with arcpy.da.UpdateCursor(out_name  + '\\' + str(shel),('source', 'GID', 'id')) as cursor:
        for row in cursor:
            row[0]='OpenStreetMap'
            row[1]=row[2]
            cursor.updateRow(row)
    

# Clean up feature layers
arcpy.Delete_management('osm')
arcpy.Delete_management('country')
arcpy.AddMessage("Delete temporary layer")
print("yes_4")


