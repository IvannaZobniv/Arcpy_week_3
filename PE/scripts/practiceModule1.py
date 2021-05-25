# This module is saved as practiceModule1.py

# The function below creates points from a list of coordinates
# Example list: [[-113,23][-120,36][-116,-2]]

def createPoints(coordinateList, featureClass):

    # Import arcpy and create an insert cursor
    import arcpy

    with arcpy.da.InsertCursor(featureClass, ("SHAPE@",)) as rowInserter:

        # Loop through each coordinate in the list and make a point    
        for coordinate in coordinateList:
            point = arcpy.Point(coordinate[0],coordinate[1])
            rowInserter.insertRow((point,))
