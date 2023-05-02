import geopandas
import json

import mapRepresentation as mr
import aStarModule as a
#import time

def getRoute(start, end, username, node1, node2, node3, node4):
    """ getRoute function
        returns a route between the requested nodes
        Example usage:
            gdf = geopandas.read_file("propertyDetails.geojson").to_json()
            gdf = json.loads(gdf)
            testStart2 = [-2.394504547119141,50.732449679036556]
            testEnd2 = [-2.4036455154418945,50.712562182791466]
            getRoute(testStart2, testEnd2, "Test1", [0,0], [0,0], [0,0], [0,0])
        parameters:
            -start, end, node1, node2, node3, node4: the nodes the user has requested a route between
            -username: the name of the farm
            -gdf: stores the geojson information
            -boundaries: stores the boundaries for the specified username
            -grid: mapRepresentation object
            -tempGrid: stores the grid produced by the mapRepresentation module
            -graph: graph object from the aStarModule
            -cords: stores the grid co-ordinates of the start and target nodes of a path
            
    """
    
    gdf = geopandas.read_file("propertyDetails.geojson").to_json()
    gdf = json.loads(gdf)
    boundaries = []
    gridRoute = []
    
    for x in range (len(gdf["features"])):
        if gdf["features"][x]["properties"]["userName"] == username:
            boundaries.append(gdf["features"][x])

    gdf = boundaries
    grid = mr.gridRep(gdf)
    tempGrid = grid.produceGrid(150,150)
    graph = a.graph()
    graph.parseGrid(tempGrid)


    #Different processes depending on the number of nodes in the requested path
    if node1 == [0,0]:
        cords = grid.stCoords(start, end)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        gridRoute = grid.routeConversion(route)
        
    elif node2 == [0,0]:
        cords = grid.stCoords(start, node1)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = grid.routeConversion(route)

        graph = a.graph()
        graph.parseGrid(tempGrid)
        cords = grid.stCoords(node1, end)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = gridRoute + grid.routeConversion(route)
        
    elif node3 == [0,0]:
        cords = grid.stCoords(start, node1)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = grid.routeConversion(route)

        graph = a.graph()
        graph.parseGrid(tempGrid)
        cords = grid.stCoords(node1, node2)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = gridRoute + grid.routeConversion(route)

        graph = a.graph()
        graph.parseGrid(tempGrid)
        cords = grid.stCoords(node2, end)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = gridRoute + grid.routeConversion(route)

    elif node4 == [0,0]:
        
        cords = grid.stCoords(start, node1)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = grid.routeConversion(route)

        graph = a.graph()
        graph.parseGrid(tempGrid)
        cords = grid.stCoords(node1, node2)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = gridRoute + grid.routeConversion(route)


        graph = a.graph()
        graph.parseGrid(tempGrid)
        cords = grid.stCoords(node2, node3)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = gridRoute + grid.routeConversion(route)


        graph = a.graph()
        graph.parseGrid(tempGrid)
        cords = grid.stCoords(node3, end)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = gridRoute + grid.routeConversion(route)
        
    elif node4 != [0,0]:
        
        cords = grid.stCoords(start, node1)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = grid.routeConversion(route)
        
        graph = a.graph()
        graph.parseGrid(tempGrid)

        cords = grid.stCoords(node1, node2)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = gridRoute + grid.routeConversion(route)
        
        graph = a.graph()
        graph.parseGrid(tempGrid)

        cords = grid.stCoords(node2, node3)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = gridRoute + grid.routeConversion(route)
        
        graph = a.graph()
        graph.parseGrid(tempGrid)

        cords = grid.stCoords(node3, node4)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = gridRoute + grid.routeConversion(route)
        
        graph = a.graph()
        graph.parseGrid(tempGrid)
        
        cords = grid.stCoords(node4, end)
        astar = a.aStar(graph, cords[0], cords[1])
        route = astar.findPath()
        route = grid.optimizeRoute(route)
        route.reverse()
        gridRoute = gridRoute + grid.routeConversion(route)

        
    return gridRoute                                                
                                                     
                                                    
#print(getRoute(testStart2, testEnd2, "Test1", [0,0], [0,0], [0,0], [0,0]))
