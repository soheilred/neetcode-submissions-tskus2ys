class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = {}

        def bt(i, op):
            if (i, op) in memo:
                return memo[(i, op)]

            if i == n:
                memo[(i, op)] = op == 0
                return op == 0
            
            if op < 0:
                memo[(i, op)] = False
                return False
            
            if s[i] == '(':
                memo[(i, op)] = bt(i + 1, op + 1)
            
            elif s[i] == ')':
                memo[(i, op)] = bt(i + 1, op - 1)

            elif s[i] == '*':
                memo[(i, op)] = bt(i+1, op) or bt(i+1, op+1) or bt(i+1, op-1)
            
            return memo[(i, op)]
        
        return bt(0, 0)

        star = 0
        max_op, min_op = 0, 0
        for c in s:
            if c == "(":
                max_op += 1
                min_op += 1
            
            elif c == ")":
                max_op -= 1
                min_op -= 1
            
            elif c == "*":
                # star += 1
                max_op += 1
                min_op -= 1
            
            # if op < 0:
            # if max_op < min_op:
            if min_op < 0:
                # if star >= op:
                    # op = 0
                # else:
                min_op = 0
                # return False
        
        # return max_op - min_op <= star
        print(max_op, min_op)
        return max_op > min_op


        # n = len(s)

        # def bt(l, r):
        #     print(l, r)
        #     if abs(r - l) == 1:
        #         return s[l] == "*" or (s[l:r+1] == '()')

        #     if l == r:
        #         return s[l] == "*"
            
        #     if l > r or s[l] == ')':
        #         return False
            
        #     if s[l] == '(':
        #         if s[r] == ')':
        #             return bt(l + 1, r - 1)
        #         if s[r] == '*':
        #             return bt(l + 1, r) or bt(l + 1, r - 1)
        #     return False


        # return bt(0, n - 1)
            
        