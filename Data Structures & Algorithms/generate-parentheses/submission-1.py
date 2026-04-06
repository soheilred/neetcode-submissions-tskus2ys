class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def gen_par(combo, left_n, right_n):
            if left_n == right_n == n:
                res.append(''.join(combo))

            if left_n < n:
                combo.append('(')
                gen_par(combo, left_n + 1, right_n)
                combo.pop()

            if right_n < n and left_n > right_n:
                combo.append(')')
                gen_par(combo, left_n, right_n + 1)
                combo.pop()
            
        gen_par([], 0, 0)
        return res

