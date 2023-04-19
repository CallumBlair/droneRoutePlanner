class gridRep():

    def __init__(self, gpd):
        self.geopandas = gpd
        self.grid = []
        self.minMax = []
        self.target = []
        self.start = []
        self.startGrid = []
        self.targetGrid = []

    def createGrid(self, sizeX, sizeY):
        grid = []
        for x in range(sizeX):
            tempgrid = []
            for y in range(sizeY):
                tempgrid.append(1)
            grid.append(tempgrid)
        self.grid = grid
        return None
        
    def outerBoundary(self):
        featureArr = self.geopandas["features"]
        maxX = featureArr[0]["geometry"]["coordinates"][0][0][0]
        maxY = featureArr[0]["geometry"]["coordinates"][0][0][1]
        minX = maxX
        minY = maxY
        
        for x in featureArr:
            if x["properties"]["boundaryType"] == "property":
                cords = x["geometry"]["coordinates"][0]
                for y in cords:
                    if y[0] > maxX:
                        maxX = y[0]
                    if y[1] > maxY:
                        maxY = y[1]
                    if y[0] < minX:
                        minX = y[0]
                    if y[1] < minY:
                        minY = y[1]
            
        self.minMax = [maxX, maxY, minX, minY]
        return None


    def ccw(self, A,B,C):
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

    def intersect(self, A,B,C,D):
        return self.ccw(A,C,D) != self.ccw(B,C,D) and self.ccw(A,B,C) != self.ccw(A,B,D)

    def markOuterBoundary(self):
        minMax = self.minMax
        grid = self.grid
        gridX = len(grid)
        gridY = len(grid[0])
        width = minMax[0] - minMax[2]
        height = minMax[1] - minMax[3]
        widthSpacing = width/gridX
        heightSpacing = height/gridY
        minX = minMax[2]
        minY = minMax[3]
        #points = []
        lines = []
        minPoint = [minX - widthSpacing, minY - heightSpacing]
        featureArr = self.geopandas["features"]
        for f in featureArr:
            if f["properties"]["boundaryType"] == "property":
                propertyBoundary = f["geometry"]["coordinates"][0]

        lines.append([propertyBoundary[0], propertyBoundary[len(propertyBoundary)-1]])
        for g in range(len(propertyBoundary)-1):
            lines.append([propertyBoundary[g], propertyBoundary[g+1]])
    
        for x in range(gridX-1):
            for y in range(gridY-1):
                bottomLeft = [(x*widthSpacing)+minX, (y*heightSpacing)+minY]
                bottomRight = [((x+1)*widthSpacing)+minX, (y*heightSpacing)+minY]
                topLeft = [(x*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                topRight = [((x+1)*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                #points.append([bottomLeft,bottomRight,topLeft,topRight,[x,y]])
                #print(bottomLeft)
                hitCounterbl = 0
                hitCounterbr = 0
                hitCountertl = 0
                hitCountertr = 0
                for s in lines:
                    if self.intersect([bottomLeft[0], bottomLeft[1]],minPoint,s[0],s[1]):
                    #and self.intersect([bottomRight[0], bottomRight[1]],minPoint,s[0],s[1]) and self.intersect([topLeft[0], topLeft[1]],minPoint,s[0],s[1]) and self.intersect([topRight[0], topRight[1]],minPoint,s[0],s[1]):
                        hitCounterbl = hitCounterbl + 1
                    if self.intersect([bottomRight[0], bottomRight[1]],minPoint,s[0],s[1]):
                        hitCounterbr = hitCounterbr + 1
                    if self.intersect([topLeft[0], topLeft[1]],minPoint,s[0],s[1]):
                        hitCountertl = hitCountertl + 1
                    if self.intersect([topRight[0], topRight[1]],minPoint,s[0],s[1]):
                        hitCountertr = hitCountertr + 1
                        
                if (hitCounterbl%2) != 0 and (hitCounterbr%2) != 0 and (hitCountertl%2) != 0 and (hitCountertr%2) != 0:
                    grid[x][y] = 0
                    
        self.grid = grid   
        return None

                        
                
    def markObstacles(self):
        minMax = self.minMax
        grid = self.grid
        gridX = len(grid)
        gridY = len(grid[0])
        width = minMax[0] - minMax[2]
        height = minMax[1] - minMax[3]
        widthSpacing = width/gridX
        heightSpacing = height/gridY
        minX = minMax[2]
        minY = minMax[3]
        #points = []
        minPoint = [minX - widthSpacing, minY - heightSpacing]
        

        
        featureArr = self.geopandas["features"]
        obstacles = []
        for f in featureArr:
            if f["properties"]["boundaryType"] == "obstacle":
                obstacles.append(f["geometry"]["coordinates"][0])
        
        
        for obstacle in obstacles:
 
            lines = []
            lines.append([obstacle[0], obstacle[len(obstacle)-1]])
            for g in range(len(obstacle)-1):
                lines.append([obstacle[g], obstacle[g+1]])

            for x in range(gridX-1):
                for y in range(gridY-1):
                    bottomLeft = [(x*widthSpacing)+minX, (y*heightSpacing)+minY]
                    bottomRight = [((x+1)*widthSpacing)+minX, (y*heightSpacing)+minY]
                    topLeft = [(x*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                    topRight = [((x+1)*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                    #points.append([bottomLeft,bottomRight,topLeft,topRight,[x,y]])
                    #print(bottomLeft)
                    hitCounterbl = 0
                    hitCounterbr = 0
                    hitCountertl = 0
                    hitCountertr = 0
                    for s in lines:
                        if self.intersect([bottomLeft[0], bottomLeft[1]],minPoint,s[0],s[1]):
                        #and self.intersect([bottomRight[0], bottomRight[1]],minPoint,s[0],s[1]) and self.intersect([topLeft[0], topLeft[1]],minPoint,s[0],s[1]) and self.intersect([topRight[0], topRight[1]],minPoint,s[0],s[1]):
                            hitCounterbl = hitCounterbl + 1
                        if self.intersect([bottomRight[0], bottomRight[1]],minPoint,s[0],s[1]):
                            hitCounterbr = hitCounterbr + 1
                        if self.intersect([topLeft[0], topLeft[1]],minPoint,s[0],s[1]):
                            hitCountertl = hitCountertl + 1
                        if self.intersect([topRight[0], topRight[1]],minPoint,s[0],s[1]):
                            hitCountertr = hitCountertr + 1
                    
                    if (hitCounterbl%2) != 0 or (hitCounterbr%2) != 0 or (hitCountertl%2) != 0 or (hitCountertr%2) != 0:
                        grid[x][y] = 1
        self.grid = grid
        return None

    def stCoords(self, start, target):
        minMax = self.minMax
        grid = self.grid
        gridX = len(grid)
        gridY = len(grid[0])
        width = minMax[0] - minMax[2]
        height = minMax[1] - minMax[3]
        widthSpacing = width/gridX
        heightSpacing = height/gridY
        minX = minMax[2]
        minY = minMax[3]
        

        startX = (start[0] - minX)/widthSpacing
        startY = (start[1] - minY)/heightSpacing
        targetX = (target[0] - minX)/widthSpacing
        targetY = (target[1] - minY)/heightSpacing
        self.startGrid = "00000" + str(int(startX))+ "00000" + str(int(startY))
        self.targetGrid = "00000" + str(int(targetX))+ "00000" + str(int(targetY))
        return [self.startGrid, self.targetGrid]
        
    def routeConversion(self, route):
        minMax = self.minMax
        grid = self.grid
        gridX = len(grid)
        gridY = len(grid[0])
        width = minMax[0] - minMax[2]
        height = minMax[1] - minMax[3]
        widthSpacing = width/gridX
        heightSpacing = height/gridY
        minX = minMax[2]
        minY = minMax[3]
        convertedRoute = []

        for stop in route:

            routeX = float(stop[0])
            routeY = float(stop[1])
            
            x = minX + (widthSpacing*routeX)
            y = minY + (heightSpacing*routeY)
            convertedRoute.append([x,y])
        return(convertedRoute)
                

        
    def produceGrid(self, sizeX, sizeY):
        self.createGrid(sizeX, sizeY)
        self.outerBoundary()
        self.markOuterBoundary()
        self.markObstacles()
        return self.grid

    
        
#rep = gridRep(gdf)
#rep.produceGrid(65,65)
#rep.createGrid(65,65)
#rep.outerBoundary()
#rep.markOuterBoundary()
#rep.markObstacles()

#for x in rep.grid:
#    print(x)
#print(rep.outerBoundary())
#sd = rep.markOuterBoundary(rep.createGrid(65,65), rep.outerBoundary())
#rep.markObstacles(sd,rep.outerBoundary())
