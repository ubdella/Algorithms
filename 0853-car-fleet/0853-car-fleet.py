class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        timeToFinish = [0]*n
        zipped = list(zip(position, speed))
        zipped.sort(key = lambda x: -x[0])
        position, speed = zip(*zipped)

        nextSlowCarTime = float('-inf')
        res = 0
        for i, pos in enumerate(position):
            timeToFinish = (target - pos)/speed[i]
            if timeToFinish > nextSlowCarTime:
                res += 1
                nextSlowCarTime = timeToFinish
        return res
