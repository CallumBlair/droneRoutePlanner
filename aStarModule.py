

#Example grids for use in testing
testGrid = [[0,0,1,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,1,1],
            [0,0,0,0,0,1,0,0,0],
            [0,0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,0,0]
            ]

testGrid2 = [[0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
             [0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0],
             [1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0],
             [0,1,1,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0],
             [0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0],
             [0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0],
             [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],              
            ]


class Node:
    """ Node class
        stores a graph node
        functions:
            __init__(cord, ident, neighbor)
            getId()
            addNeighbor(neightborId, weight)
            numNeighbor()
            getNeighbors()
            details()
    """
    
    def __init__(self, cord, ident, neighbor = None):
        """ __init__
            Initalizes self attributes
            parameters:
                -self.id: stores the id of the node
                -self.x: stores the x coordinate of the node
                -self.y: stores the y coordinate of the node
                -self.h: stores the heuristic value of the node
                -self.distStart: stores the distance of the node from the starting node
                -self.parent: stores the nodes parent
                -self.neighbors: stores a two dimensional array storing each neighbor and the weighting of the path between the nodes
        """
        self.id = str(ident)
        self.x = cord[0]
        self.y = cord[1]
        self.h = -1
        self.distStart = None
        self.parent = None
        if neighbor == None:
            self.neighbors = []
        else:
            self.neighbors = neighbor
    
    def getId(self):
        """ getId
            returns the nodes id value
        """
        return str(self.id)

    def addNeighbor(self, neighborId,weight):
        """ addNeighbor
            adds a node as a neighbor with the paths weight
            parameters:
                -neighborId: the node being added as a neighbors Id value
                -weight: the weight of the path between the two nodes
        """
        if neighborId not in self.neighbors:    
            self.neighbors.append([neighborId,weight])
        return None

    def numNeighbor(self):
        """ numNeighbor
            returns the number of neighbors the node has
        """
        return len(self.neighbors)

    def getNeighbors(self):
        """ getNeighbors
            returns the two dimensional array of neighbors
        """
        return self.neighbors

    def details(self):
        """ details
            used for debugging, returns all the main attributes of the node
        """
        string = str(self.id)
        string += " coords: " + str(self.x) + "," + str(self.y)
        string += ", h: " + str(self.h)
        string += ", dist_start: " + str(self.distStart)
        string += ", parent: " + str(self.parent)
        string += ", neighbors" + str(self.neighbors)
        return string



class graph:
    """ graph class
        allows for the creation of a graph built of Node elements from a two dimensional grid
        functions:
            __init__()
            addNode(cord, ident, neighbor)
            addNodes(nodes)
            getNode(node)
            getNodes()
            addEdge(node1, node2, weight)
            addStart(nodeId)
            parseGrid(grid)
            parseNeighbors(coOrd, grid)
        
    """
    def __init__(self):
        """ __init__
            Initializes self attributes
            parameters:
                -self.nodeDict: a dictionary of all the nodes making up the graph
                -self.numNodes: stores the total number of nodes
        """
        self.nodeDict = {}
        self.numNodes = 0
        
    def addNode(self, cord, ident, neighbor=None):
        """ addNode
            adds a node to the dictionary
            parameters:
                -cord: the coordinate of the noded
                -the node Id
                -neighbors: any neighbors to be added on creation
                -node: the Node object to be added to the graph
        """
        node = Node(cord, ident, neighbor)
        self.nodeDict[node.getId()] = node
        self.numNodes = self.numNodes + 1

    def addNodes(self, nodes=[[]]):
        """ addNode
            adds multiple nodes provided in an array
        """
        for x in range (len(nodes)):
            self.addNode(nodes[x][0],nodes[x][1])
         
    def getNode(self, node):
        """ getNode
            returns a node
        """
        return self.nodeDict[node]
    def getNodes(self):
        """ getNodes
            returns all node Id's
        """
        return self.nodeDict.keys()

    def addEdge(self, node1, node2, weight):
        """ addEdge
            adds an edge between two nodes
        """
        node1 = str(node1)
        node2 = str(node2)
        if node1 in self.nodeDict.keys() and node2 in self.nodeDict.keys():
            self.nodeDict[node1].addNeighbor(node2,weight)
            self.nodeDict[node2].addNeighbor(node1,weight)

    def addStart(self, nodeId):
        """ addStart
            sets the start node
        """
        self.startNode = str(nodeId)

    def parseGrid(self, grid):
        """ parseGrid
            creates a graph from a given grid in a two dimensional array
        """
        self.nodeDict = {}
        self.numNodes = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                currentCord = [x,y]
                currentId = "00000" + str(x) + "00000" + str(y)
                
                if grid[x][y] == 0:
                    self.addNode(currentCord,currentId)
                    currentNeighbor = self.parseNeighbors(currentCord, grid)
                    for z in currentNeighbor:
                        self.addEdge(currentId, str(z),1)
                    
                
    def parseNeighbors(self, coOrd, grid):
        """ parseNeighbors
            returns a list of the up to eight neighbors of a square in the grid
        """
        maxX = len(grid)-1
        maxY = len(grid[0])-1
        x = coOrd[0]
        y = coOrd[1]
        neighborCord = []
        neighborId = []
        neighborCord.append([x-1,y+1])
        neighborCord.append([x-1,y])
        neighborCord.append([x-1,y-1])
        neighborCord.append([x,y+1])
        neighborCord.append([x,y-1])
        neighborCord.append([x+1,y+1])
        neighborCord.append([x+1,y])
        neighborCord.append([x+1,y-1])
        for cord in neighborCord:
            if cord[0] >= 0 and cord[0] <= maxX and cord[1] >= 0 and cord[1] <= maxY:
                neighborId.append("00000" + str(cord[0]) + "00000" + str(cord[1]))
        return neighborId
                
class aStar():
    """ aStar class
        performs the A Star algorithm on a graph to find one of the shortest paths between the start and target nodes

        functions:
            __init__(graph, startNodeId, targetNodeId)
            manhattan(node1, node2)
            distance(parent, child)
            hValue(parent, child, target)
            openedEmpty()
            removeOpened()
            findPath()
            displayPath()
        ExampleUsage:
            graph = graph()
            graph.parseGrid(testGrid2)
            astar = aStar(graph, "000000000000", "0000032000000")
            route = astar.findPath()
            astar.displayImage(testGrid2)
    """
    def __init__(self, graph, startNodeId, targetNodeId):
        """ __init__
            Initializes self attributes
            parameters:
                -self.graph: the graph object
                -self.startId: the id of the start node
                -self.targetId: the id of the target node
                -self.start: the start node object
                -self.target: the target node object
                -self.open: open array
                -self.closed: closed array
                -self.steps: number of steps to achieve the path
                -self.route: array holding the final route
        """
        self.graph = graph
        self.startId = startNodeId
        self.targetId = targetNodeId
        self.start = graph.getNode(startNodeId)
        self.target = graph.getNode(targetNodeId)
        self.open = []
        self.closed = []
        self.steps = 0
        self.route = []
        
    def manhattan(self, node1, node2):
        """ manhattan
            returns the manhattan distance between two nodes
        """
        return abs(node1.x - node2.x) + abs(node1.y - node2.y)

    def distance(self, parent, child):
            """ distance
                returns the distance between a child node and the start node
            """
            for x in parent.neighbors:
                if x[0] == child.getId():
                    weight = x[1]
            distance = parent.distStart + weight

            
            if child.parent == None:
                child.parent = parent
            if child.distStart == None:
                child.distStart = distance

            
            if distance < child.distStart:
                child.parent = parent
                child.distStart = distance
                return distance
            return child.distStart
                    
    def hValue(self, parent, child, target):
        """ hValue
            returns the estimated distance from the start node to the target node via the current node (Heuristic Value)
        """
        h = self.distance(parent, child) + self.manhattan(child, target)
        child.h = h
        return h

    def openedEmpty(self):
        """ openedEmpty
            returns True if the open array is empty
        """
        if self.open != []:
            return True
        else:
            return False
        
    def removeOpened(self):
        """ remove Opened
            returns the lowest node in the open list
        """
        lowestNode = self.open[0]
        for x in self.open:
            if x.h < lowestNode.h:
                lowestNode = x
        return lowestNode
        
    def findPath(self):
        """ find Path
            utlilizes the A Star algorithm to find the shortest path between the set start and target nodes
        """
        self.open.append(self.start)
        self.start.distStart = 0
        self.start.h = self.manhattan(self.start, self.target)
        notComplete = True
        
        while self.openedEmpty() and notComplete:
            currentNode = self.removeOpened()
            self.open.remove(currentNode)
            self.closed.append(currentNode)
            if currentNode == self.target:
                notComplete = False
            
            for nodes in currentNode.neighbors:
                
                node = self.graph.getNode(nodes[0])
                if node not in self.closed:
                    if node not in self.open:
                        self.open.append(node)
                    cost = self.hValue(currentNode, node, self.target)
                    
        route = []
        nodes = self.target
        routeIncomplete = True
        route.append(nodes.getId())
        while routeIncomplete:
            
            route.append(nodes.parent.getId())
            nodes = nodes.parent
            if nodes == self.start:
                routeIncomplete = False
        
        self.route = route
        cordRoute = []
        for x in route:
            cordRoute.append([self.graph.getNode(x).x,self.graph.getNode(x).y])
    
        return(cordRoute)

    def displayImage(self, grid):
        """ displayImage
            Displays the grid, with the shortest path indicated by the value 3
        """
        route = self.route
        array = []
        for stops in route:
                array.append([self.graph.getNode(stops).x,self.graph.getNode(stops).y])
        for z in array:
            grid[z[0]][z[1]] = 3
        for p in grid:
            print(p)
        





