class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # we are given a 2d array of 1s and 0s representing an image
        # image[i][j] is the value of that image
        # perform a "flood fill" starting from the given pixel sr sc
        
        # What is a flood fill?
        # Check adjacent pixels of the same color and change them to 'color'

        ROWS = len(image)
        COLUMNS = len(image[0])

        original_color = image[sr][sc]

        visited = set()

        if color == original_color:
            return image

        def dfs(r, c, original_color):
            if r < 0 or c< 0 or r == ROWS or c == COLUMNS or image[r][c] != original_color or (r,c) in visited:
                return -1

            visited.add((r,c))
            image[r][c] = color


            dfs(r-1,c, original_color)
            dfs(r+1,c, original_color)
            dfs(r,c-1, original_color)
            dfs(r,c+1, original_color)

            return 0

        dfs(sr,sc, original_color)
        return image

