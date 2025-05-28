import heapq 
import itertools

class PrioridadQueue:
    def __init__(self):
        self._heap = []
        self._counter = itertools.count()
    
    def push(self, item, prioridad):
        count=next(self._counter)
        heapq.heappush(self._heap, (prioridad, count, item))

    def pop(self):
        if not self._heap:
            raise None 
        return heapq.heappop(self._heap)[-1]
    
    def size(self):
        return len(self._heap)

    def is_empty(self):
        return len(self._heap) == 0