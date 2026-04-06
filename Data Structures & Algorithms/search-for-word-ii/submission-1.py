class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        res = set()

        def dfs(i, j, w, k):
            # print(i, j, w, k)
            if k >= len(w):
                return True
            
            # if board[i][j] != w[k]:
                # return False
            
            tmp = board[i][j]
            board[i][j] = '*'
            res = False
            for (di, dj) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                new_i, new_j = i + di, j + dj
                if not -1 < new_i < n or not -1 < new_j < m or board[new_i][new_j] == '*':
                    continue
                
                if board[new_i][new_j] == w[k]:
                    res = res or dfs(new_i, new_j, w, k+1)
                
                # else:
                    # res = res or dfs(new_i, new_j, w, k)
            board[i][j] = tmp
            return res

        for w in words:
            for i in range(n):
                for j in range(m):
                    # print(w, board[i][j], i, j)
                    if board[i][j] != w[0]:
                        continue
                    if dfs(i, j, w, 1):
                        res.add(w)

        return list(res)
                
            
        