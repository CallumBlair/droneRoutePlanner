import geopandas
import json

import mapRepresentation as mr
import aStarModule as a


#testStart = [-2.409343,50.713762]
#testEnd = [-2.394243, 50.731368]

testStart = [-2.385585, 50.725952]
testEnd = [-2.391425, 50.713372]



gdf = geopandas.read_file("propertyDetails.geojson").to_json()
gdf = json.loads(gdf)

grid = mr.gridRep(gdf)

tempGrid = grid.produceGrid(150,150)
cords = grid.stCoords(testStart, testEnd)

graph = a.graph()
graph.parseGrid(tempGrid)
astar = a.aStar(graph, cords[0], cords[1])
route = astar.findPath()
#astar.displayImage(tempGrid)
grid.routeConversion(route)

#print(route)

#"00000" + 
