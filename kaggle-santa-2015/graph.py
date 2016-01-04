
from haversine import haversine
from operator import attrgetter
import array
from binaryheap import Heap

class Edge:
    def __init__(self, v1, v2, distance):
        self.v1 = v1
        self.v2 = v2
        self.distance = distance
        
    def __str__(self):
        return "Edge(v1" + str(self.v1) + ",v2:" + str(self.v2) + ",dist:" + str(self.distance) + ")"
    
    def __repr__(self):
        return Edge(self.v1, self.v2, self.distance)    
    
    def edge_compare(self, other):
        if self.distance < other.distance:
            return -1
        elif self.distance > other.distance:
            return +1
        else:
            return 0
    
def findGifts(gifts, lat1, lat2, long1, long2):
    giftsInRange = []
    
    for giftId in gifts:
        gift = gifts[giftId]
        latitudeLower = False
        latitudeUpper = False
        if (gift.latitude > lat1):
            latitudeLower = True
        if (gift.latitude < lat2):
            latitudeUpper = True
        longitudeOk = False
        if (long1 < -180.0):
            if (gift.longitude > long1) and (gift.longitude < long2):
                longitudeOk = True
            if (gift.longitude > (long1 + 360.0)):
                longitudeOk = True
        elif (long2 > 180.0):
            if (gift.longitude > long1) and (gift.longitude < long2):
                longitudeOk = True
            if (gift.longitude < (long2 - 360.0)):
                longitudeOk = True
        else:
            if (gift.longitude > long1) and (gift.longitude < long2):
                longitudeOk = True             
        if latitudeLower == True and latitudeUpper == True and longitudeOk == True:
            giftsInRange.append(gift)
            
    return giftsInRange

def createEdges(gifts):
    
    minLat = -90.0
    maxLat = +90.0
    minLong = -180.0
    maxLong = +180.0
    
    latRange = 90
    longRange = 90
    
    k = 20
    
    edges = []
    
    for lat in range(0, latRange):
        print("lat: " + str(lat) + ", #edges:" + str(len(edges)))
        
        for long in range(0, longRange):
            lat1 = minLat + (maxLat - minLat) * ((lat) / latRange)
            lat2 = minLat + (maxLat - minLat) * ((lat + 1.0) / latRange)
            long1 = minLong + (maxLong - minLong) * ((long) / longRange)
            long2 = minLong + (maxLong - minLong) * ((long + 1.0) / longRange)
             
            lat3 = minLat + (maxLat - minLat) * ((lat - 1.0) / latRange)
            lat4 = minLat + (maxLat - minLat) * ((lat + 2.0) / latRange)
            long3 = minLong + (maxLong - minLong) * ((long - 1.0) / longRange)
            long4 = minLong + (maxLong - minLong) * ((long + 2.0) / longRange)
#             print("lat1: " + str(lat1) + ", lat2: " + str(lat2) + ", long1: " + str(long1) + ", long2: " + str(long2))
#             print("lat3: " + str(lat3) + ", lat4: " + str(lat4) + ", long3: " + str(long3) + ", long4: " + str(long4))
             
            giftsInRange = findGifts(gifts, lat1, lat2, long1, long2)
            giftsInRange2 = findGifts(gifts, lat3, lat4, long3, long4)
            
#             print("\t" + str(len(giftsInRange)))
#             print("\t" + str(len(giftsInRange2)))
            
            for gift1 in giftsInRange:
                
                edgeCandidates = []
                
                for gift2 in giftsInRange2:
                    if gift1 != gift2:
                        distance = haversine((gift1.latitude, gift1.longitude), (gift2.latitude, gift2.longitude))
                        edge = Edge(gift1.ID, gift2.ID, distance)
                        edgeCandidates.append(edge)

                edgeCandidatesSorted = sorted(edgeCandidates, key = attrgetter('distance'))

                counter = 0
                        
                for edge in edgeCandidatesSorted:
                    edges.append(edge)
                    counter = counter + 1
                    if counter == k:
                        break
            
             
            #print("#edges:" + str(len(edges)))
    
    return edges
    
def gisEdges(edges, gifts, outputFile):
    
    edgeId = 0
    
    output = open(outputFile, 'w')
    output.write("edgeID;distance;wkt\n")
    
    for edge in edges:
        output.write(str(edgeId) + ";" + str(edge.distance) + ";")
        gift1 = gifts[edge.v1]
        gift2 = gifts[edge.v2]
        output.write("LINESTRING(" + str(gift1.longitude) + " " + str(gift1.latitude) + ",")
        output.write(str(gift2.longitude) + " " + str(gift2.latitude) + ")\n")
        edgeId = edgeId + 1

    output.close()
        
def saveDownEdges(edges, gifts, outputFile):

    edgeId = 0
    
    output = open(outputFile, 'w')
    output.write("v1,v2\n")
    
    for edge in edges:
        output.write(str(edge.v1) + "," + str(edge.v2) + "\n")
        edgeId = edgeId + 1

    output.close()
    
def loadEdges(gifts, fileName):
    
    edges = []
    
    firstLine = True
    # open the file
    with open(fileName) as infile:
        # read line by line
        for line in infile:                
            # remove newline character from the end
            line = line.rstrip()
            
            # parse header
            if firstLine == True:
                firstLine = False
                continue

            # split the line
            splittedLine = line.split(',')
            
            v1 = int(splittedLine[0])
            v2 = int(splittedLine[1])
            
            gift1 = gifts[v1]
            gift2 = gifts[v2]
            
            distance = haversine((gift1.latitude, gift1.longitude), (gift2.latitude, gift2.longitude))
            edge = Edge(gift1.ID, gift2.ID, distance)
            
            edges.append(edge)
            
    return edges            

def findClosestGifts(gifts, giftList, giftsToConnect):
    
    k = 5
    
    edges = []
    
    for gift1Id in giftsToConnect:
        gift1 = gifts[gift1Id]
        edgeCandidates = []
        for gift2 in giftList:
            if gift1 != gift2:
                distance = haversine((gift1.latitude, gift1.longitude), (gift2.latitude, gift2.longitude))
                edge = Edge(gift1.ID, gift2.ID, distance)
                edgeCandidates.append(edge)

        edgeCandidatesSorted = sorted(edgeCandidates, key = attrgetter('distance'))

        counter = 0
                        
        for edge in edgeCandidatesSorted:
            edges.append(edge)
            counter = counter + 1
            if counter == k:
                break
    
    return edges

def addEdgeToNeigbour(neighbours, edgeId, v1, v2, distance):
    if v1 not in neighbours:
        neighbours[v1] = []
    
    v1Neigbours = neighbours[v1]
    
    edgeAlreadyIn = False
    
    for edge in v1Neigbours:
        if edge.v2 == v2:
            edgeAlreadyIn = True
    
    if edgeAlreadyIn == False:
        edge = Edge(v1, v2, distance)
        edge.edgeId = edgeId
        v1Neigbours.append(edge)
    

def mst(edges, gifts):
    
    mstEdges = []
    
    visited = array.array('i',(0 for i in range(0,len(gifts)+10)))
    
    #print("#edges: " + str(len(edges)))
    
    edgesSorted = sorted(edges, key = attrgetter('distance'))
    
#     for edge in edgesSorted:
#         print(str(edge))
        
    #print("Sorted...")
    
    neighbours = {}
    edgeId = 0
    
    for edge in edgesSorted:
        # add edge v1->v2
        addEdgeToNeigbour(neighbours, edgeId, edge.v1, edge.v2, edge.distance)
        #edgeId = edgeId + 1
        # add edge v2->v1
        addEdgeToNeigbour(neighbours, edgeId, edge.v2, edge.v1, edge.distance)
        edgeId = edgeId + 1
        
    heap = Heap()
            
    while True:
        
        #print("iteration... #bh:" + str(heap.size()) + ", #mstEdges: " + str(len(mstEdges)))
                
        if heap.size() == 0:
            visitedCounter = 0
            for i in visited:
                visitedCounter = visitedCounter + i
            if visitedCounter < len(visited):
                # find a new edge to start
                for edge in edgesSorted:
                    if visited[edge.v1] == 0 and visited[edge.v2] == 0:
                        print("shortestEdge: " + str(edge))
                        mstEdges.append(edge)
                        visited[edge.v1] = 1
                        visited[edge.v2] = 1
                        for n in neighbours[edge.v1]:
                            heap.push(n.distance, n.edgeId)
                        for n in neighbours[edge.v2]:
                            heap.push(n.distance, n.edgeId)
                        break
                         
        if heap.size() == 0:
            break
                
        edgeId = heap.pop()
        edge = edgesSorted[edgeId]
        #print("edge from bh: " + str(edge))
        
        nextVertex = None
        
        if visited[edge.v1] == 0:
            nextVertex = edge.v1
        elif visited[edge.v2] == 0:
            nextVertex = edge.v2
        else:
            continue
        
        mstEdges.append(edge)
        visited[nextVertex] = 1
    
        for n in neighbours[nextVertex]:
            heap.push(n.distance, n.edgeId)
                
    return mstEdges

def keepOnlyCaseStudyEdges(edges):
    edgesToRemain = []
    allowedVerticies = [56028, 57331, 3905, 38452, 62723, 5227, 70427, 12673,
                        50544, 12284, 5509, 75292, 61446, 45037, 84225, 80940,
                        98019, 48669, 72479, 33270, 47210, 21630]
    for edge in edges:
        if edge.v1 in allowedVerticies or edge.v2 in allowedVerticies:
            edgesToRemain.append(edge)
    
    return edgesToRemain

def unifySubGraphs(edges, gifts):
    
    # double the edges
    edges2 = []
    for edge in edges:
        reverseEdge = Edge(edge.v2, edge.v1, edge.distance)
        edges2.append(reverseEdge)
    for edge in edges:
        edges2.append(edge)
    
    # build neighbours:
    neighbours = {}
    for edge in edges2:
        if edge.v1 not in neighbours:
            neighbours[edge.v1] = []
        neighbours[edge.v1].append(edge)
            
    # run tree traversal
    visitedVertex = array.array('i',(0 for i in range(0,len(gifts)+2)))
    previousVertex = array.array('i',(0 for i in range(0,len(gifts)+2)))
    
    groups = []
    group = []
    
    
    # find groups with one node:
    for i in gifts:
        if i not in neighbours:
            visitedVertex[i] = 1
            groups.append([i])
            
    for i in gifts:
        if i in neighbours:
            start = i
            current = i
            previousVertex[i] = i
            break
    
    while True:
        #print("current: " + str(current))
        if visitedVertex[current] == 0:
            group.append(current)
        visitedVertex[current] = 1
        
        nextEdge = None
        for edge in neighbours[current]:
            if visitedVertex[edge.v2] == 0:
                nextEdge = edge
                break
        
        if nextEdge == None:
            current = previousVertex[current]
        else:
            previousVertex[nextEdge.v2] = current
            current = nextEdge.v2
        
        currentHasMoreNeighbours = False
        for edge in neighbours[current]:
            if visitedVertex[edge.v2] == 0:
                currentHasMoreNeighbours = True
                break
        
        if current == start and currentHasMoreNeighbours == False:
            groups.append(group)
            group = []
            newStart = False
            for i in range(0, len(gifts)+2):
                if visitedVertex[i] == 0 and i in neighbours:
                    start = i
                    current = i
                    previousVertex[i] = i
                    #print("new start at " + str(i))
                    newStart = True
                    break
            if newStart == False:
                break

    print("groups: " + str(len(groups)))
    for group in groups:
        print("group size: " + str(len(group)))
        if len(group) < 1000:
            minDistance = float("inf")
            minv1 = -1
            minv2 = -1
            for v in group:
                gift1 = gifts[v]
                for giftId in gifts:
                    gift2 = gifts[giftId] 
                    distance = haversine((gift1.latitude, gift1.longitude), (gift2.latitude, gift2.longitude))
                    if giftId not in group and distance < minDistance:
                        minDistance = distance
                        minv1 = v
                        minv2 = giftId
#            print("group: " + str(group))
            edge = Edge(minv1, minv2, minDistance)
            edges.append(edge)
            #print(str(edge))
    return edges

def createGiftOrder(edges, gifts):
        # find the closest node to the north pole
        closestGiftId = -1
        closestDistance = float("inf") 
        for giftId in gifts:
            gift = gifts[giftId]
            distance = haversine((gift.latitude, gift.longitude), (90, 0))
            if distance < closestDistance:
                closestGiftId = giftId
                closestDistance = distance 
        
        print("closestGift: " + str(gifts[closestGiftId]))
        
        # double the edges
        edges2 = []
        for edge in edges:
            reverseEdge = Edge(edge.v2, edge.v1, edge.distance)
            edges2.append(reverseEdge)
        for edge in edges:
            edges2.append(edge)
        
        # add edgeId to edges
        for i in range(0, len(edges2)):
            edges2[i].edgeId = i
        
        # build neighbours:
        neighbours = {}
        for edge in edges2:
            if edge.v1 not in neighbours:
                neighbours[edge.v1] = []
            neighbours[edge.v1].append(edge)
        
        # run tree traversal
        visitedVertex = array.array('i',(0 for i in range(0,len(gifts)+2)))
        previousVertex = array.array('i',(0 for i in range(0,len(gifts)+2)))
        
        order = []
        
        current = closestGiftId
        
        while True:
            if visitedVertex[current] == 0:
                order.append(current)
            visitedVertex[current] = 1
            
            nextEdge = None
            for edge in neighbours[current]:
                if visitedVertex[edge.v2] == 0:
                    nextEdge = edge
                    break
            
            if nextEdge == None:
                current = previousVertex[current]
            else:
                previousVertex[nextEdge.v2] = current
                current = nextEdge.v2
                
            if current == closestGiftId:
                break
            
        return order
    
def writeOutOrderGIS(order, outputFile, gifts):
    
    output = open(outputFile, 'w')
    output.write("pathId;wkt\n")
    
    output.write("0;LINESTRING(0.0 90.0")
    for giftId in order:
        if giftId == -2:
            continue
        gift = gifts[giftId]
        output.write("," + str(gift.longitude) + " " + str(gift.latitude))
        
    output.write(")\n")
    output.close()

def writeOutOrder(order, outputFile):
    output = open(outputFile, 'w')
    for o in order:
        output.write(str(o) + "\n")
    output.close()

# test case for gifts with longitude -179, 179...
# gifts = {12: Gift(12, 179.0, -89.0, 10.0) }
# giftInRange = findGifts(gifts, -92.0, -88.0, -182.0, -178.0)
# print(str(giftInRange))

def addEdge(mstEdges, gifts, id1, id2):
    gift1 = gifts[id1]
    gift2 = gifts[id2]
    distance = haversine((gift1.latitude, gift1.longitude), (gift2.latitude, gift2.longitude))
    mstEdges.append(Edge(id1, id2, distance))
    