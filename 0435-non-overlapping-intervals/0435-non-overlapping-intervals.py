class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        lastEnd = intervals[0][1]
        erases = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < lastEnd:
                erases += 1
                lastEnd = min(intervals[i][1], lastEnd)
                continue
            lastEnd = intervals[i][1]
            
        return(erases)