class Solution:
	def hoursTaken(self, piles, k):
		hours = 0
		for pile in piles:
			hours += math.ceil(pile / k)
		return hours
			
	def minEatingSpeed(self, piles, h) -> int:
		low = 1
		high = max(piles)
		while low < high:
			mid = (low + high) // 2
			if self.hoursTaken(piles, mid) > h:
				low = mid + 1
			else:
				high = mid
		return low
                
                