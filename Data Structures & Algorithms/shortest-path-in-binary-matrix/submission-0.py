class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0]:
            return -1

        ROWS = len(grid)
        COLUMNS = len(grid[0])
        visited = set()
        queue = deque()

        target = (ROWS-1,COLUMNS-1)

        length = 1

        queue.append((0,0))
        visited.add((0,0))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if (r,c) == target:
                    return length

                for ro in range(-1,2):
                    for co in range(-1,2):
                        if (ro,co) == (0,0):
                            continue

                        rs, cs = r+ro, c+co

                        if min(rs,cs) < 0 or rs == ROWS or cs == COLUMNS or grid[rs][cs] or (rs,cs) in visited:
                            continue
                        visited.add((rs,cs))
                        queue.append((rs,cs))

            length+=1

        return -1
        

