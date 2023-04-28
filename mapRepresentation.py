class gridRep():
    """ gridRep class
        allows for the creation and usage of grids that represent real world enviroments
        usage:
            gdf = geopandas.read_file("propertyDetails.geojson").to_json()
            gdf = json.loads(gdf)
            boundaries = []
            for x in range (len(gdf["features"])):
                if gdf["features"][x]["properties"]["userName"] == "Test1":
                    boundaries.append(gdf["features"][x])

            gdf = boundaries
            rep = gridRep(gdf)
            rep.produceGrid(30,30)
                
        functions:
            __init__(gpd)
            createGrid(sizeX, sizeY)
            createPreGrid(sizeX, sizeY, multi)
            outerBoundary()
            ccw(A,B,C)
            intersect(A,B,C,D)
            markPreOuterBoundary()
            markPreObstacles()
            updateGrid()
            markOuterBoundary()
            markObstacles()
            stCoords(start, target)
            routeConversion(route)
            produceGrid(sizeX, sizeY)
    """
    def __init__(self, gpd):
        """ __init__
            Initializes self attributes
            parameters:
                self.geopandas: stores the geopandas data
                self.grid: stores the final grid
                self.preGrid: stores the pre-pass lower resolution grid
                self.minMax: stores the minimum and maximum X and Y values for the grid
                self.target: stores the target lat-lng
                self.start: stores the start lat-lng
                self.startGrid: stores the start grid coordinates
                self.targetGrid: stores the target grid coordinates
        """
        self.geopandas = gpd
        self.grid = []
        self.preGrid = []
        self.minMax = []
        self.target = []
        self.start = []
        self.startGrid = []
        self.targetGrid = []

    def createGrid(self, sizeX, sizeY):
        """ createGrid
            creates a grid of the given size storing it in self.grid
            parameters:
                grid: used to store the temporary two dimensional array when creating the grid
        """
        grid = []
        for x in range(sizeX):
            tempgrid = []
            for y in range(sizeY):
                tempgrid.append(1)
            grid.append(tempgrid)
        self.grid = grid
        return None

    def createPreGrid(self, sizeX, sizeY, multi):
        """ createPreGrid
            creates a grid of the given size storing it in self.preGrid
            parameters:
                grid: used to store the temporary two dimensional array when creating the grid
        """
        grid = []
        for x in range(int(sizeX/multi)):
            tempgrid = []
            for y in range(int(sizeY/multi)):
                tempgrid.append(1)
            grid.append(tempgrid)
        self.preGrid = grid
        return None

        
    def outerBoundary(self):
        """ outerBoundary
            generates the min and max X and Y values for the created grid
            storing these values in self.minMax
        """
        featureArr = self.geopandas
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
        """ ccw
            checks if the three given points are in counter clockwise order
        """
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

    def intersect(self, A,B,C,D):
        """ intersect
            returns if the two lines A-B and C-D intersect            
        """
        return self.ccw(A,C,D) != self.ccw(B,C,D) and self.ccw(A,B,C) != self.ccw(A,B,D)




    def markPreOuterBoundary(self):
        """ markPreOuterBoundary
            sets the area within the property boundary to 0 within the preGrid
            parameters:
                -minMax: self.minMax
                -grid: self.grid
                -gridX: the max length of the grid on the X axis
                -gridY: the max length of the grid on the Y axis
                -width = the width of the grid in the real world lat-lng
                -height = the height of the grid in the real world lat-lng
                -widthSpacing: the width of each square in the grid in the real world
                -heightSpacing: the height of each square in the grid in the real world
                -minX: the minimum X value
                -minY: the minimum Y value
                -lines: array that will store each line making up the property polygon
                -minPoint: stores a point outside the grid at the equivalent of -1,-1
                
        """
        minMax = self.minMax
        grid = self.preGrid
        gridX = len(grid)
        gridY = len(grid[0])
        width = minMax[0] - minMax[2]
        height = minMax[1] - minMax[3]
        widthSpacing = width/gridX
        heightSpacing = height/gridY
        minX = minMax[2]
        minY = minMax[3]
        lines = []
        
        minPoint = [minX - widthSpacing, minY - heightSpacing]
        
        featureArr = self.geopandas
        for f in featureArr:
            if f["properties"]["boundaryType"] == "property":
                propertyBoundary = f["geometry"]["coordinates"][0]

        lines.append([propertyBoundary[0], propertyBoundary[len(propertyBoundary)-1]])
        for g in range(len(propertyBoundary)-1):
            lines.append([propertyBoundary[g], propertyBoundary[g+1]])
    
        for x in range(gridX-1):
            for y in range(gridY-1):
                if grid[x][y] != 0:
                    bottomLeft = [(x*widthSpacing)+minX, (y*heightSpacing)+minY]
                    bottomRight = [((x+1)*widthSpacing)+minX, (y*heightSpacing)+minY]
                    topLeft = [(x*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                    topRight = [((x+1)*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                    
                    hitCounterbl = 0
                    hitCounterbr = 0
                    hitCountertl = 0
                    hitCountertr = 0
                    
                    for s in lines:
                        if self.intersect([bottomLeft[0], bottomLeft[1]],minPoint,s[0],s[1]):
                            hitCounterbl = hitCounterbl + 1
                        if self.intersect([bottomRight[0], bottomRight[1]],minPoint,s[0],s[1]):
                            hitCounterbr = hitCounterbr + 1
                        if self.intersect([topLeft[0], topLeft[1]],minPoint,s[0],s[1]):
                            hitCountertl = hitCountertl + 1
                        if self.intersect([topRight[0], topRight[1]],minPoint,s[0],s[1]):
                            hitCountertr = hitCountertr + 1
                            
                    if (hitCounterbl%2) != 0 and (hitCounterbr%2) != 0 and (hitCountertl%2) != 0 and (hitCountertr%2) != 0:
                        grid[x][y] = 0
                    
        self.preGrid = grid
        return None



    def markPreObstacles(self):
        """ markPreObstacles
            marks the areas of the preGrid that fall within an obstacle
            parameters:
                -minMax: self.minMax
                -grid: self.grid
                -gridX: the max length of the grid on the X axis
                -gridY: the max length of the grid on the Y axis
                -width = the width of the grid in the real world lat-lng
                -height = the height of the grid in the real world lat-lng
                -widthSpacing: the width of each square in the grid in the real world
                -heightSpacing: the height of each square in the grid in the real world
                -minX: the minimum X value
                -minY: the minimum Y value
                -minPoint: stores a point outside the grid at the equivalent of -1,-1
                
        """
        minMax = self.minMax
        grid = self.preGrid
        gridX = len(grid)
        gridY = len(grid[0])
        width = minMax[0] - minMax[2]
        height = minMax[1] - minMax[3]
        widthSpacing = width/gridX
        heightSpacing = height/gridY
        minX = minMax[2]
        minY = minMax[3]
        
        minPoint = [minX - widthSpacing, minY - heightSpacing]
        
        featureArr = self.geopandas
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
                    if grid[x][y] == 0:
                        bottomLeft = [(x*widthSpacing)+minX, (y*heightSpacing)+minY]
                        bottomRight = [((x+1)*widthSpacing)+minX, (y*heightSpacing)+minY]
                        topLeft = [(x*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                        topRight = [((x+1)*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                        
                        hitCounterbl = 0
                        hitCounterbr = 0
                        hitCountertl = 0
                        hitCountertr = 0
                        for s in lines:
                            if self.intersect([bottomLeft[0], bottomLeft[1]],minPoint,s[0],s[1]):
                                hitCounterbl = hitCounterbl + 1
                            if self.intersect([bottomRight[0], bottomRight[1]],minPoint,s[0],s[1]):
                                hitCounterbr = hitCounterbr + 1
                            if self.intersect([topLeft[0], topLeft[1]],minPoint,s[0],s[1]):
                                hitCountertl = hitCountertl + 1
                            if self.intersect([topRight[0], topRight[1]],minPoint,s[0],s[1]):
                                hitCountertr = hitCountertr + 1
                        
                        if (hitCounterbl%2) != 0 or (hitCounterbr%2) != 0 or (hitCountertl%2) != 0 or (hitCountertr%2) != 0:
                            grid[x][y] = 1
        self.preGrid = grid
        return None


    def updateGrid(self,multi):
        """ updateGrid
            transfers the lower-resolution preGrid information to the main grid
        """
        preGrid = self.preGrid
        grid = self.grid

        for x in range(len(grid)):
            for y in range(len(grid)):
                preGridX = int(x/multi)
                preGridY = int(y/multi)
                if preGrid[preGridX][preGridY] == 0:
                    grid[x][y] = 0
                else:
                    grid[x][y] = 1
        self.grid = grid
    

    def markOuterBoundary(self):
        """ markOuterBoundary
            sets the area within the property boundary to 0 within the Grid
            parameters:
                -minMax: self.minMax
                -grid: self.grid
                -gridX: the max length of the grid on the X axis
                -gridY: the max length of the grid on the Y axis
                -width = the width of the grid in the real world lat-lng
                -height = the height of the grid in the real world lat-lng
                -widthSpacing: the width of each square in the grid in the real world
                -heightSpacing: the height of each square in the grid in the real world
                -minX: the minimum X value
                -minY: the minimum Y value
                -lines: array that will store each line making up the property polygon
                -minPoint: stores a point outside the grid at the equivalent of -1,-1
        """
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

        lines = []
        minPoint = [minX - widthSpacing, minY - heightSpacing]
 
        featureArr = self.geopandas
        for f in featureArr:
            if f["properties"]["boundaryType"] == "property":
                propertyBoundary = f["geometry"]["coordinates"][0]

        lines.append([propertyBoundary[0], propertyBoundary[len(propertyBoundary)-1]])
        for g in range(len(propertyBoundary)-1):
            lines.append([propertyBoundary[g], propertyBoundary[g+1]])
    
        for x in range(gridX-1):
            for y in range(gridY-1):
                if grid[x][y] != 0:
                    bottomLeft = [(x*widthSpacing)+minX, (y*heightSpacing)+minY]
                    bottomRight = [((x+1)*widthSpacing)+minX, (y*heightSpacing)+minY]
                    topLeft = [(x*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                    topRight = [((x+1)*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                    hitCounterbl = 0
                    hitCounterbr = 0
                    hitCountertl = 0
                    hitCountertr = 0
                    for s in lines:
                        if self.intersect([bottomLeft[0], bottomLeft[1]],minPoint,s[0],s[1]):
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
        """ markObstacles
            marks the areas of the Grid that fall within an obstacle
            parameters:
                -minMax: self.minMax
                -grid: self.grid
                -gridX: the max length of the grid on the X axis
                -gridY: the max length of the grid on the Y axis
                -width = the width of the grid in the real world lat-lng
                -height = the height of the grid in the real world lat-lng
                -widthSpacing: the width of each square in the grid in the real world
                -heightSpacing: the height of each square in the grid in the real world
                -minX: the minimum X value
                -minY: the minimum Y value
                -minPoint: stores a point outside the grid at the equivalent of -1,-1
                
        """
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

        minPoint = [minX - widthSpacing, minY - heightSpacing]
        
        featureArr = self.geopandas
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
                    if grid[x][y] == 0:
                        bottomLeft = [(x*widthSpacing)+minX, (y*heightSpacing)+minY]
                        bottomRight = [((x+1)*widthSpacing)+minX, (y*heightSpacing)+minY]
                        topLeft = [(x*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                        topRight = [((x+1)*widthSpacing)+minX, ((y+1)*heightSpacing)+minY]
                        
                        hitCounterbl = 0
                        hitCounterbr = 0
                        hitCountertl = 0
                        hitCountertr = 0
                        for s in lines:
                            if self.intersect([bottomLeft[0], bottomLeft[1]],minPoint,s[0],s[1]):
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
        """ stCoords
            returns the grid coordinates of the start and target nodes
            parameters:
                -minMax: self.minMax
                -grid: self.grid
                -gridX: the max length of the grid on the X axis
                -gridY: the max length of the grid on the Y axis
                -width = the width of the grid in the real world lat-lng
                -height = the height of the grid in the real world lat-lng
                -widthSpacing: the width of each square in the grid in the real world
                -heightSpacing: the height of each square in the grid in the real world
                -minX: the minimum X value
                -minY: the minimum Y value
        """
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
        """ routeConversion
            converts the grid coordinate route to a lat-lng route and returns this route
            parameters:
                -minMax: self.minMax
                -grid: self.grid
                -gridX: the max length of the grid on the X axis
                -gridY: the max length of the grid on the Y axis
                -width = the width of the grid in the real world lat-lng
                -height = the height of the grid in the real world lat-lng
                -widthSpacing: the width of each square in the grid in the real world
                -heightSpacing: the height of each square in the grid in the real world
                -minX: the minimum X value
                -minY: the minimum Y value
                -convertedRoute: array that stores the converted route
        """
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
        """ produceGrid
            a function simplifying the process of creating a grid buy condensing all the main steps into a single function
            returning the final grid
        """
        self.createGrid(sizeX, sizeY)
        self.createPreGrid(sizeX, sizeY,5)
        self.outerBoundary()
        
        self.markPreOuterBoundary()
        self.markPreObstacles()
        self.updateGrid(5)
        
        self.markOuterBoundary()
        self.markObstacles()
        return self.grid




