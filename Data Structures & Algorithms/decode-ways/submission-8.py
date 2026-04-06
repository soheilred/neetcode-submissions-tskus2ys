class Solution:
    def numDecodings(self, s: str) -> int:
        total = 0
        n = len(s)
        cache = {}

        # @lru_cache
        def bt(i):
            # print(i)
            # nonlocal total
            if i >= n:
                # cache[i] = True
                # total += 1
                return 1
            
            if s[i] == '0':
                # cache[i] = False
                return 0

            res = bt(i + 1)
            if i < n - 1 and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
                res += bt(i + 2)
            
            # else:
                # res += 
            
            return res
                
            # if s[i+1] == '0':
                # return bt(i + 2)
            
            # cache[i] = bt(i + 1) or bt(i + 2)
            # return cache[i]
        
        # bt(0)
        return bt(0)
            
        