class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        timeToFinish = [0]*n
        zipped = list(zip(position, speed))
        zipped.sort(key = lambda x: -x[0])
        position, speed = zip(*zipped)
        #10 8 5 3 0
        #2 4 1 3 1
        
        for i in range(n):
            timeToFinish[i] = (target - position[i]) / speed[i]
        
        nextSlowCarTime = float('-inf')
        res = 0
        for i, pos in enumerate(position):
            if timeToFinish[i] > nextSlowCarTime:
                res += 1
                nextSlowCarTime = timeToFinish[i]
        return res
