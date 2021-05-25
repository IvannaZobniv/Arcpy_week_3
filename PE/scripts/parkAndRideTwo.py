# This script determines the percentage of cities with two park and ride facilities
import arcpy
arcpy.env.overwriteOutput = True
cityBoundaries=r'D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\PE\Lesson3PracticeExercises\Lesson3PracticeExerciseB\Washington.gdb\CityBoundaries'
parkAndRide=r'D:\MY\KNU\3_COURSE\2_Semertr\Programing_GIS\My_work\Arcpy_week_3\PE\Lesson3PracticeExercises\Lesson3PracticeExerciseB\Washington.gdb\ParkAndRide'
parkAndRideField = "HasTwoParkAndRides" # Name of column for storing the Park & Ride information
cityIDStringField = "CI_FIPS"  # Name of column with city IDs
citiesWithTwoParkAndRides = 0  # Used for counting cities with at least two P & R facilities
numCities = 0  # Used for counting cities in total
# Make a feature layer of all the park and ride facilities
arcpy.MakeFeatureLayer_management(parkAndRide, "ParkAndRideLayer")
# Make an update cursor and loop through each city
with arcpy.da.UpdateCursor(cityBoundaries, (cityIDStringField, parkAndRideField)) as cityRows:
    for city in cityRows:
    # Create a query string for the current city
        cityIDString = city[0]
        queryString = '"' + cityIDStringField + '" = ' + "'" + cityIDString + "'"
        # Make a feature layer of just the current city polygon    
        arcpy.MakeFeatureLayer_management(cityBoundaries, "CurrentCityLayer", queryString)
        try:
            # Narrow down the park and ride layer by selecting only the park and rides in the current city
            arcpy.SelectLayerByLocation_management("ParkAndRideLayer", "CONTAINED_BY", "CurrentCityLayer")
            # Count the number of park and ride facilities selected
            selectedParkAndRideCount = arcpy.GetCount_management("ParkAndRideLayer")
            numSelectedParkAndRide = int(selectedParkAndRideCount.getOutput(0))
            # If more than two park and ride facilities found, update the row to TRUE
            if numSelectedParkAndRide >= 2:
                city[1] = "TRUE"
                # Don't forget to call updateRow
                cityRows.updateRow(city)
                # Add 1 to your tally of cities with two park and rides 
                citiesWithTwoParkAndRides += 1
        finally:
            # Delete current cities layer to prepare for next run of loop
            arcpy.Delete_management("CurrentCityLayer")
            numCities +=1
# Clean up park and ride feature layer
arcpy.Delete_management("ParkAndRideLayer")
# Calculate and report the number of cities with two park and rides
if numCities <> 0:
    percentCitiesWithParkAndRide = ((1.0 * citiesWithTwoParkAndRides) / numCities) * 100
else:
    print "Error with input dataset. No cities found."
print str(percentCitiesWithParkAndRide) + " percent of cities have two park and rides."
