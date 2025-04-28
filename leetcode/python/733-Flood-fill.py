class Solution:
    def coloring(self, image, sr, sc, color, current):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]): return

        if current != image[sr][sc]: return

        image[sr][sc] = color

        self.coloring(image, sr-1, sc, color, current)
        self.coloring(image, sr+1, sc, color, current)
        self.coloring(image, sr, sc-1, color, current)
        self.coloring(image, sr, sc+1, color, current)

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color: return image

        self.coloring(image, sr, sc, color, image[sr][sc])
        return image

test = Solution()
output = test.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print(output)