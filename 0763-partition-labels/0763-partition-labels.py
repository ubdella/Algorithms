class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def getPos(c):
            return ord(c) - ord('a')
        endPos = [0] * 26
        for i in range(len(s)):
            endPos[getPos(s[i])] = i
        res = []
        i = j = 0
        splitPos = endPos[getPos(s[0])]
        while j < len(s):
            if j == splitPos:
                res.append(j - i + 1)
                i = j + 1
                if i < len(s):
                    splitPos = endPos[getPos(s[i])]
            if endPos[getPos(s[j])] > splitPos:
                splitPos = endPos[getPos(s[j])]   
            j += 1 
        return res