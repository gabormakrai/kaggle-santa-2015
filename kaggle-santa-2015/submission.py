from haversine import haversine

def loadOrder(fileName):
    print("Loading order from " + fileName + "...")

    order = []
    
    # open the file
    with open(fileName) as infile:
        # read line by line
        for line in infile:                
            # remove newline character from the end
            line = line.rstrip()
            
            order.append(int(line))
                        
    print("Done... #order: " + str(len(order)))
    
    return order

def doSubmissionFromOrder(order, gifts):
    
    sleighMaxWeight = 1000.0
    currentWeight = 0.0
    currentTrip = []
    
    trips = []
    
    for giftId in order:
        gift = gifts[giftId]
        if currentWeight + gift.weight > sleighMaxWeight:
            trips.append(currentTrip)
            currentWeight = gift.weight
            currentTrip = [gift]
        else:
            currentTrip.append(gift)
            currentWeight = currentWeight + gift.weight
    trips.append(currentTrip)

#     counter = 0    
#     for trip in trips:
#         tripWeight = 0
#         for gift in trip:
#             counter = counter + 1
#             tripWeight = tripWeight + gift.weight
#         print(str(tripWeight))
#     print("order: " + str(len(order)))
#     print("counter: " + str(counter))
    
    return trips

def calculateWRW(trips, gifts):
    of = 0.0
    for trip in trips:
        tripWeight = 0.0
        for gift in trip:
            tripWeight = tripWeight + gift.weight
        # add north pole to first gift weight
        of = of + haversine((90.0, 0.0), (trip[0].latitude, trip[0].longitude)) * (tripWeight + 10.0)
        # add last gift to north pole
        of = of + haversine((trip[len(trip) - 1].latitude, trip[len(trip) - 1].longitude), (90.0, 0.0)) * (10.0)
        previousGift = None
        for gift in trip:
            if previousGift == None:
                previousGift = gift
                tripWeight = tripWeight - previousGift.weight
            else:
                currentGift = gift
                of = of + haversine((currentGift.latitude, currentGift.longitude), (previousGift.latitude, previousGift.longitude)) * (tripWeight + 10.0)
                tripWeight = tripWeight - currentGift.weight
                previousGift = currentGift
    return of

def createSubmissionFromTrips(trips, fileName):
    tripId = 1
    
    output = open(fileName, 'w')
    output.write("GiftId,TripId\n")
    
    for trip in trips:
        for gift in trip:
            output.write(str(gift.ID) + "," + str(tripId) + "\n")
        tripId = tripId + 1
    
    output.close()
    