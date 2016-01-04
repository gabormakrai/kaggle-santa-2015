from haversine import haversine
from random import randint

def optimizeOrder(gifts, order):
    orderLength = calculatePathLength(gifts, order)
    
    iterationLimit = 10000
    
    iteration = 0
    print("length: " + str(orderLength))
    
    while (True):
        iteration = iteration + 1
        if iteration == iterationLimit:
            break
        print("iteration " + str(iteration))
        orderLength = optimizeOrderIteration(gifts, order, orderLength)
    

# index1 -> index1 + 1 -> index1 + 2
# index2 -> index2 + 1 -> index2 + 2
    
def optimizeOrderIteration(gifts, order, currentLength):

    while (True):
    
        index1 = randint(0, len(order) - 310)
        
        betterFound = False
        betterIndex1 = -1
        betterIndex2 = -1
        betterLength = 0.0
        
        for index2 in range(index1 + 3, index1 + 300):
            length = currentLength
            
            length = length - distance(order[index1], order[index1 + 1], gifts)
            length = length - distance(order[index1 + 1], order[index1 + 2], gifts)
            length = length - distance(order[index2], order[index2 + 1], gifts)
            length = length - distance(order[index2 + 1], order[index2 + 2], gifts)
            
            length = length + distance(order[index1], order[index2 + 1], gifts)
            length = length + distance(order[index2 + 1], order[index1 + 2], gifts)
            length = length + distance(order[index2], order[index1 + 1], gifts)
            length = length + distance(order[index1 + 1], order[index2 + 2], gifts)
            
            if (currentLength > length):
                print("current: " + str(currentLength) + ", iterLength: " + str(length))
                betterIndex1 = index1 + 1
                betterIndex2 = index2 + 1 
                betterFound = True
                betterLength = length
                break
                
        if betterFound == True:
            temp = order[betterIndex1]
            order[betterIndex1] = order[betterIndex2]
            order[betterIndex2] = temp
            return betterLength

def distance(gift1Id, gift2Id, gifts):
    gift1 = gifts[gift1Id]
    gift2 = gifts[gift2Id]
    return haversine((gift1.latitude, gift1.longitude), (gift2.latitude, gift2.longitude))

def calculatePathLength(gifts, order):
    length = 0.0
    previousGift = None
    for giftId in order:
        if previousGift == None:
            previousGift = gifts[giftId]
        else:
            currentGift = gifts[giftId]
            distance = haversine((currentGift.latitude, currentGift.longitude), (previousGift.latitude, previousGift.longitude))
            length = length + distance
            previousGift = currentGift
    return length