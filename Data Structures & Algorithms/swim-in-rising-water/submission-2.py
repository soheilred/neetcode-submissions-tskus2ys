class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        seen = set()
        memo = {}
        maxH = minH = grid[0][0]
        for i in range(n):
            maxH = max(maxH, max(grid[i]))
            minH = max(minH, min(grid[i]))

        def bt(i, j, hw):
            # print(i, j, hw)
            if not -1 < min(i, j) <= max(i, j) < n or (i, j) in seen or grid[i][j] > hw:
                return False
            
            if i == n - 1 and j == n - 1:
                return True

            # if grid[i][j] > hw:
            hw = max(grid[i][j], hw)

            seen.add((i, j))
            res =  bt(i - 1, j, hw) or \
                   bt(i, j - 1, hw) or \
                   bt(i + 1, j, hw) or \
                   bt(i, j + 1, hw)
                
            seen.remove((i, j))
            # memo[(i, j)] = max(hw, res) if res != float('inf') else hw

            return res

        for h in range(minH, maxH):
            if bt(0, 0, h):
                return h
            seen = set()
        
        return maxH
        