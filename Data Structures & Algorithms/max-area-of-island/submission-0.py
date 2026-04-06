class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        n, m = len(grid), len(grid[0])
        
        def iseland_area(i, j, area):
            if -1 < i < n and -1 < j < m and grid[i][j] == 1:
                grid[i][j] = 0
                area += 1 +\
                    iseland_area(i + 1, j, area) +\
                    iseland_area(i, j + 1, area) +\
                    iseland_area(i - 1, j, area) +\
                    iseland_area(i, j - 1, area)

            return area
        

        for i in range(n):
            for j in range(m):
                max_area = max(max_area, iseland_area(i, j, 0))
        
        return max_area
        