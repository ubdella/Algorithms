class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        stack = [] # (index, temperature)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                topI, _ = stack.pop()
                answer[topI] = i - topI
            stack.append((i, t))
        return answer
                    