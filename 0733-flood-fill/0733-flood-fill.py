class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pc = image[sr][sc]
        self.fill(image, sr, sc, pc, color)
        return image
    def fill(self, image, sr, sc, pc, color):
        if sc<0 or sc>len(image[0])-1 or sr>len(image)-1 or sr<0 or image[sr][sc]!=pc or image[sr][sc] == color:
            return image
        image[sr][sc] = color
        self.fill(image, sr+1, sc, pc, color)
        self.fill(image, sr-1, sc, pc, color)
        self.fill(image, sr, sc+1, pc, color)
        self.fill(image, sr, sc-1, pc, color)