class KthLargest:
    def __init__(self, k, nums):
        self.scores = nums
        self.k = k
        heapq.heapify(self.scores)
        while len(self.scores) > k:
            heapq.heappop(self.scores)
    def add(self, val):
        heapq.heappush(self.scores, val)
        if len(self.scores) > self.k:
            heapq.heappop(self.scores)
            
        return self.scores[0]