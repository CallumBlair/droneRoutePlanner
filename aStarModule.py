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
            [0,0,0,0,0,1,0,0,0]]

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


startNode = [0,0]
#targetNode = [7,8]
targetNode = [0,32]

openList = []
closedList = []

class Node:
    def __init__(self, cord, ident, neighbor = None):
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
        return str(self.id)

    def addNeighbor(self, neighborId):
        if neighborId not in self.neighbors:    
            self.neighbors.append(neighborId)

    def numNeighbor(self):
        return len(self.neighbors)

    def getNeighbors(self):
        return self.neighbors

    def details(self):
        string = str(self.id)
        string += " coords: " + str(self.x) + "," + str(self.y)
        string += ", h: " + str(self.h)
        string += ", dist_start: " + str(self.distStart)
        string += ", parent: " + str(self.parent)
        string += ", neighbors" + str(self.neighbors)
        return string



class graph:
    def __init__(self):
        self.nodeDict = {}
        self.numNodes = 0
        
    def addNode(self, cord, ident, neighbor=None):
        node = Node(cord, ident, neighbor)
        self.nodeDict[node.getId()] = node
        self.numNodes = self.numNodes + 1

    def addNodes(self, nodes=[[]]):
        for x in range (len(nodes)):
            self.addNode(nodes[x][0],nodes[x][1])
         
    def getNode(self, node):
        return self.nodeDict[node]
    def getNodes(self):
        return self.nodeDict.keys()

    def addEdge(self, node1, node2):
        node1 = str(node1)
        node2 = str(node2)
        if node1 in self.nodeDict.keys() and node2 in self.nodeDict.keys():
            self.nodeDict[node1].addNeighbor(node2)
            self.nodeDict[node2].addNeighbor(node1)


    def addStart(self, nodeId):
        self.startNode = str(nodeId)

    def parseGrid(self, grid):
        self.nodeDict = {}
        self.numNodes = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                currentCord = [x,y]
                currentId = "00000" + str(x) + "00000" + str(y)
                #print("id" + str(currentId))
                if grid[x][y] == 0:
                    self.addNode(currentCord,currentId)
                    currentNeighbor = self.parseNeighbors(currentCord, grid)
                    for z in currentNeighbor:
                        self.addEdge(currentId, str(z))
                    
                
    def parseNeighbors(self, coOrd, grid):
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

    def __init__(self,graph, startNodeId, targetNodeId):
        self.graph = graph
        self.startId = startNodeId
        self.targetId = targetNodeId
        self.start = graph.getNode(startNodeId)
        self.target = graph.getNode(targetNodeId)
        self.open = []
        self.closed = []
        self.steps = 0
        
    def manhattan(self, node1, node2):
        return abs(node1.x - node2.x) + abs(node1.y - node2.y)

    def distance(self, parent, child):
            distance = parent.distStart + 1

            
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
        h = self.distance(parent, child) + self.manhattan(child, target)
        child.h = h
        return h

    def openedEmpty(self):
        if self.open != []:
            return True
        else:
            return False
    def removeOpened(self):
        lowestNode = self.open[0]
        for x in self.open:
            if x.h < lowestNode.h:
                lowestNode = x
        return lowestNode
        
    def findPath(self):
        self.open.append(self.start)
        self.start.distStart = 0
        self.start.h = self.manhattan(self.start, self.target)
        notComplete = True
        
        while self.openedEmpty() and notComplete:
            currentNode = self.removeOpened()
            #print(currentNode.details())
            self.open.remove(currentNode)
            self.closed.append(currentNode)
            if currentNode == self.target:
                notComplete = False
                #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            for nodes in currentNode.neighbors:
                #print(nodes)
                node = self.graph.getNode(nodes)
                if node not in self.closed:
                    if node not in self.open:
                        self.open.append(node)
                    cost = self.hValue(currentNode, node, self.target)
                    #print("COST" + str(cost))
        #print(notComplete)
        route = []
        nodes = self.target
        routeIncomplete = True
        route.append(nodes.getId())
        while routeIncomplete:
            #print(nodes.details())
            route.append(nodes.parent.getId())
            nodes = nodes.parent
            if nodes == self.start:
                routeIncomplete = False
        #print(route)
        return(route)

    def displayImage(self, grid, route):
        array = []
        for stops in route:
                array.append([self.graph.getNode(stops).x,self.graph.getNode(stops).y])
        for z in array:
            grid[z[0]][z[1]] = 3
##        for g in range(len(grid)):
##            af = ""
##            for k in range(len(grid[1])):
##                if grid[g][k] == 0:
##                    af = af + " "
##                else:
##                    af = af + str(grid[g][k])
##            print(af)
        for p in grid:
            print(p)
        

graph = graph()
##graph.addNode([1,1],1)
##graph.addNode([1,2],2)
##graph.addEdge(1,2)
##graph.addEdge(1,2)
##print(graph.getNode("1").details())
graph.parseGrid(testGrid2)
#print(graph.getNodes())
#str(00000)
#astar = aStar(graph, "000000000000", "000007000008")
astar = aStar(graph, "000000000000", "0000032000000")
#print(astar.manhattan(graph.getNode("00"),graph.getNode("78")))
route = astar.findPath()
astar.displayImage(testGrid2,route)
#graph.parseNeighbors([5,5], testGrid)

##graph = graph()
##
##graph.addNode([1,1],1)
##graph.addNode([1,2],2)
##graph.addNodes([[[1,1],3],[[2,2],4]])
##graph.addEdge(3,2)
##print(graph.getNode("3").details())
##graph.addEdge(3,1)
##print(graph.getNode("3").details())
##print(graph.getNodes())


