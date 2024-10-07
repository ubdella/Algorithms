class Solution:
	def spiralMatrix(self, m, n, head):
		
		# initialize borders, matrix with -1, i,j,direction variable
		top, bottom = -1, m
		start, end = -1, n
		matrix = [[-1] * n for _ in range(m)]
		dire = 'right'
		i,j = 0,0
		
		# traverse through the matrix until the head becomes null and update it
		while head:
			matrix[i][j] = head.val
			head = head.next
			if dire == 'right':
				if j == end - 1:
					dire = 'down'
					i += 1
					top += 1
				else:
					j += 1
			elif dire == 'down':
				if i == bottom - 1:
					dire = 'left'
					j -= 1
					end -= 1
				else:
					i += 1
			elif dire == 'left':
				if j == start + 1:
					dire = 'up'
					i -= 1
					bottom -= 1
				else:
					j -= 1
			elif dire == 'up':
				if i == top + 1:
					dire = 'right'
					j += 1
					start += 1
				else:
					i -= 1
		return matrix
