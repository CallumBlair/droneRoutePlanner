import geopandas
import json

import mapRepresentation as mr
import aStarModule as a


#testStart = [-2.409343,50.713762]
#testEnd = [-2.394243, 50.731368]

#testStart = [-2.385585, 50.725952]
#testEnd = [-2.391425, 50.713372]


#testStart2 = [-2.394504547119141,50.732449679036556]
#testEnd2 = [-2.4036455154418945,50.712562182791466]

#testStart2 = [50.732449,-2.394504]
#testEnd2 =   [50.712562,-2.403645]


#gdf = geopandas.read_file("propertyDetails.geojson").to_json()
#gdf = json.loads(gdf)

def getRoute(start, end, username):
    gdf = geopandas.read_file("propertyDetails.geojson").to_json()
    gdf = json.loads(gdf)
    boundaries = []
    
    
    for x in range (len(gdf["features"])):
        if gdf["features"][x]["properties"]["userName"] == username:
            boundaries.append(gdf["features"][x])

    gdf = boundaries
    #boundaries = json.dumps(boundaries)
    
    grid = mr.gridRep(gdf)

    tempGrid = grid.produceGrid(150,150)
    cords = grid.stCoords(start, end)

    graph = a.graph()
    graph.parseGrid(tempGrid)
    astar = a.aStar(graph, cords[0], cords[1])
    route = astar.findPath()
    #astar.displayImage(tempGrid)
    return grid.routeConversion(route)

    #print(route)

    #"00000" + 

#print(getRoute(testStart2, testEnd2))
