class Solution:
	def lexicalOrder(self, n):
		result = []
		current = 1
		result.append(current)
		for i in range(n - 1):
			if current * 10 <= n:
				current = current * 10
			else:
				while current % 10 == 9 or current + 1 > n:
					current = current // 10
				current += 1
			result.append(current)
		return result