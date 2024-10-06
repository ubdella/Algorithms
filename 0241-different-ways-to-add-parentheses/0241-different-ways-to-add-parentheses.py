from typing import List
import operator

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def evaluate(nums, ops):
            stack = [nums[0]]
            for i, op in enumerate(ops):
                for num in nums[i+1:]:
                    if op == '+':
                        stack.append(stack.pop() + num)
                    elif op == '-':
                        stack.append(stack.pop() - num)
                    elif op == '*':
                        stack.append(stack.pop() * num)
                    stack, num = num, stack.pop()
                stack.append(num)
            return stack

        def generate_all_ways(nums, ops):
            if not ops:
                return nums
            results = []
            for i in range(len(ops)):
                left = generate_all_ways(nums[:i+1], ops[:i])
                right = generate_all_ways(nums[i+1:], ops[i+1:])
                for l in left:
                    for r in right:
                        if ops[i] == '+':
                            results.append(l + r)
                        elif ops[i] == '-':
                            results.append(l - r)
                        elif ops[i] == '*':
                            results.append(l * r)
            return results

        nums = []
        ops = []
        num = 0
        for char in expression:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                nums.append(num)
                num = 0
                ops.append(char)
        nums.append(num)

        return generate_all_ways(nums, ops)