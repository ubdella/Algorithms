from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.point_counts = defaultdict(int)
        self.points = []

    def add(self, point):
        x, y = point
        self.point_counts[(x, y)] += 1
        self.points.append((x, y))

    def count(self, point):
        qx, qy = point
        count = 0

        for x, y in self.points:
            if abs(qx - x) == abs(qy - y) and qx != x and qy != y:
                count += self.point_counts[(x, qy)] * self.point_counts[(qx, y)]

        return count