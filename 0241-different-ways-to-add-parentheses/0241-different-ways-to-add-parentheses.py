class Solution:
	def evaluate(self, a,b,opr):
		if opr =='-':
			return a - b
		if opr =='+':
			return a + b
		if opr == '*':
			return a * b
	def diffWaysToCompute(self, expression):
		operatorsIndices = []
		for i in range(len(expression)):
			if not expression[i].isdigit():
				operatorsIndices.append(i)
		if not operatorsIndices:
			return [int(expression)]
		result = []
		for index in operatorsIndices:
			left = self.diffWaysToCompute(expression[:index])
			right = self.diffWaysToCompute(expression[index + 1:])
			for num1 in left:
				for num2 in right:
					result.append(self.evaluate(num1, num2, expression[index]))
		return result