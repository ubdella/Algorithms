class Solution:
	def lexicalOrder(self, n):
		result = []
		current = 1
		for i in range(n):
			result.append(current)            
			if current * 10 <= n:
				current = current * 10
			else:
				while current % 10 == 9 or current + 1 > n:
					current = current // 10
				current += 1

		return result