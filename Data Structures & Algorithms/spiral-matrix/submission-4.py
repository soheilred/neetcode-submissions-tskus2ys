class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        l, r, t, b = 0, m, 0, n
        res = []

        while l < r and t < b:
            print(t, b, l, r)
            for j in range(l, r):
                # print(j)
                res.append(matrix[t][j])
            
            t += 1
            for i in range(t, b):
                # print('f',i)
                res.append(matrix[i][r-1])
            
            r -= 1
            if not (l < r and t < b):
                break

            for j in range(r-1, l-1, -1):
                # print(i)
                res.append(matrix[b-1][j])
            
            b -= 1
            for i in range(b-1, t-1, -1):
                # print(j)
                res.append(matrix[i][l])
            
            l += 1
        
        return res

        