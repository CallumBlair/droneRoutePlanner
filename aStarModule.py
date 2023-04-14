testGrid = [[0,0,1,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,1,1],
            [0,0,0,0,0,1,0,0,0],
            [0,0,0,0,0,1,0,0,0],
            [0,0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,0,0]]
startNode = [0,0]
targetNode = [7,6]

openList = []
closedList = []

class Node:
    def __init__(self, cord, ident, neighbor = None):
        self.id = str(ident)
        self.x = cord[0]
        self.y = cord[1]
        self.h = 0
        self.distStart = -1
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
                currentId = str(x) + str(y)
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
                neighborId.append(str(cord[0]) + str(cord[1]))
        return neighborId
                
        
graph = graph()
##graph.addNode([1,1],1)
##graph.addNode([1,2],2)
##graph.addEdge(1,2)
##graph.addEdge(1,2)
##print(graph.getNode("1").details())
graph.parseGrid(testGrid)
print(graph.getNodes())
astar = aStar(graph, "00", "76")
print(astar.manhattan(graph.getNode("00"),graph.getNode("76")))

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


