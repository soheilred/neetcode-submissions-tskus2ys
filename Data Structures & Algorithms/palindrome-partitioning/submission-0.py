class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def solve(path, ind):
            print(path, ind)
            if ind == n:
                res.append(path.copy())
                return
            
            if ind > n:
                return
            
            for i in range(ind, n):
                print(s[ind:i], s[ind:i][::-1])
                if s[ind:i+1] == s[ind:i+1][::-1]:
                    path.append(s[ind:i+1])
                    solve(path, i+1)
                    path.pop()
        
        solve([], 0)
        return res

