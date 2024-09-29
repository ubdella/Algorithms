from collections import defaultdict
class DetectSquares:
    def __init__(self):
        self.ref = defaultdict(int)
        
    def add(self, point):
        self.ref[(point[0], point[1])] += 1
        
    def count(self, point):
        result = 0
        for curPoint in self.ref.keys():
            if (point[0], point[1]) == curPoint:	continue

            if abs(curPoint[0] - point[0]) != abs(curPoint[1] - point[1]):	continue

            if (curPoint[0], point[1]) in self.ref and (point[0], curPoint[1]) in self.ref:
                result += self.ref[curPoint] * self.ref[(curPoint[0], point[1])] * self.ref[(point[0], curPoint[1])]

        return result