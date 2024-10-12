class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        nearestCandleRight = [0] * n
        nearestCandleLeft = [0] * n
        prefixSums = [0] * n
        prevRight, prevLeft = -1, n

        for i in range(n):
            if s[n - i - 1] == '|':
                prevRight = n - i - 1
            if s[i] == '|':
                prevLeft = i
            nearestCandleRight[n - 1 - i] = prevRight
            nearestCandleLeft[i] = prevLeft
        prefixSums[0] = 1 if s[0] == '*' else 0
        for i in range(1,n):
            prefixSums[i] = prefixSums[i-1] + int(s[i] == '*')
        print(prefixSums)
        answer = []
        for query in queries:
            leftMostCandle = nearestCandleRight[query[0]]
            rightMostCandle = nearestCandleLeft[query[1]]
            if leftMostCandle != -1 and rightMostCandle != n and leftMostCandle < rightMostCandle:

                answer.append(prefixSums[rightMostCandle] - prefixSums[leftMostCandle])
            else:
                answer.append(0)
        return answer
                    
        
                    
            
        