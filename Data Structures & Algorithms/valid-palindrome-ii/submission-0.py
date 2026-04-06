class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        def bt(start, end, rem):
            if rem < 0:
                return False
            
            if start > end:
                return True
            
            if s[start] != s[end]:
                return bt(start, end - 1, rem - 1) or bt(start + 1, end, rem - 1)
            
            return bt(start + 1, end - 1, rem)
        
        return bt(0, n - 1, 1)
        