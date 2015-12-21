# source: https://joernhees.de/blog/2010/07/19/min-heap-in-python/

import heapq
class Heap(object):
    """ A neat min-heap wrapper which allows storing items by priority
        and get the lowest item out first (pop()).
        Also implements the iterator-methods, so can be used in a for
        loop, which will loop through all items in increasing priority order.
        Remember that accessing the items like this will iteratively call
        pop(), and hence empties the heap! """
    
    def __init__(self):
        """ create a new min-heap. """
        self._heap = []
    
    def push(self, priority, item):
        """ Push an item with priority into the heap.
            Priority 0 is the highest, which means that such an item will
            be popped first."""
        assert priority >= 0
        heapq.heappush(self._heap, (priority, item))
    
    def pop(self):
        """ Returns the item with lowest priority. """
        item = heapq.heappop(self._heap)[1] # (prio, item)[1] == item
        return item

    def size(self):
        return len(self._heap)

# TEST

# heap = Heap()
# heap.push(1.0, 1)
# heap.push(2.0, 2)
# heap.push(3.0, 3)
# heap.push(1.0, 4)
# heap.push(2.0, 5)
# 
# print(str(heap.pop()))
# print("size: " + str(len(heap._heap)))
# print(str(heap.pop()))
# print("size: " + str(len(heap._heap)))
# print(str(heap.pop()))
# print("size: " + str(len(heap._heap)))
# print(str(heap.pop()))
# print("size: " + str(len(heap._heap)))
# print(str(heap.pop()))
# print("size: " + str(len(heap._heap)))
# print(str(heap.pop()))
# print("size: " + str(len(heap._heap)))
# print(str(heap.pop()))
# print("size: " + str(len(heap._heap)))
