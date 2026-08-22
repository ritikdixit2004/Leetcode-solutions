import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap for the smaller half (invert values to use Python's min-heap)
        self.small = []
        # Min-heap for the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # 1. Add to the max-heap (small half) by default
        heapq.heappush(self.small, -num)
        
        # 2. Ensure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # 3. Rebalance the heaps if the size difference is greater than 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If odd number of elements, the extra one is in the small heap
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # If even, take the average of the top elements of both heaps
        return (-self.small[0] + self.large[0]) / 2.0