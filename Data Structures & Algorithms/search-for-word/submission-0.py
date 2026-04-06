class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        L = len(word)
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = [[False] * m for _ in range(n)]
        end = False

        def dfs(i, j, k, seen):
            print(i, j, k)
            if k == L:
                return True
            
            if k > L or not -1 < i < n or not -1 < j < m or seen[i][j] == True or board[i][j] != word[k]:
                return False
            
            seen[i][j] = True
            res = False
            for d in dirs:
                new_i = i + d[0]
                new_j = j + d[1]
                res = res or dfs(new_i, new_j, k + 1, seen)
            seen[i][j] = False
            return res
            
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0, visited):
                    return True
        return False
        