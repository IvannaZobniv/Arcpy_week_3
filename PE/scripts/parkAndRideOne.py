# This script determines the percentage of cities in the state with park and ride facilities
import arcpy
arcpy.env.overwriteOutput = True
cityBoundaries=r'D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\PE\Lesson3PracticeExercises\Lesson3PracticeExerciseA\Washington.gdb\CityBoundaries'
parkAndRide=r'D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\PE\Lesson3PracticeExercises\Lesson3PracticeExerciseA\Washington.gdb\ParkAndRide'
parkAndRideField = "HasParkAndRide"    # Name of column with Park & Ride information
citiesWithParkAndRide = 0     # Used for counting cities with Park & Ride
try:
    # Make a feature layer of all the park and ride facilities
    arcpy.MakeFeatureLayer_management(parkAndRide, "ParkAndRideLayer")
    # Make a feature layer of all the cities polygons
    arcpy.MakeFeatureLayer_management(cityBoundaries, "CitiesLayer")
except:
    print "Could not create feature layers"
try:
    # Narrow down the cities layer to only the cities that contain a park and ride
    arcpy.SelectLayerByLocation_management("CitiesLayer", "CONTAINS", "ParkAndRideLayer")
    # Create an update cursor and loop through the selected records
    with arcpy.da.UpdateCursor("CitiesLayer", (parkAndRideField,)) as cursor:
        for row in cursor:
            # Set the park and ride field to TRUE and keep a tally
            row[0] = "True"
            cursor.updateRow(row)
            citiesWithParkAndRide +=1
# Delete the feature layers even if there is an exception (error) raised
finally: 
    arcpy.Delete_management("ParkAndRideLayer")
    arcpy.Delete_management("CitiesLayer")
# Count the total number of cities (this tool saves you a loop)
numCitiesCount = arcpy.GetCount_management(cityBoundaries)
numCities = int(numCitiesCount.getOutput(0))
# Calculate the percentage and print it for the user
percentCitiesWithParkAndRide = ((1.0 * citiesWithParkAndRide) / numCities) * 100
print str(percentCitiesWithParkAndRide) + " percent of cities have a park and ride."
