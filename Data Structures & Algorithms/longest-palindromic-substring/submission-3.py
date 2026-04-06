class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = -float('inf')
        start = 0

        for i in range(n):
            # odd palindroms
            l, r = i, i
            while -1 < l <= r < n and s[l] == s[r]:
                # print(l, r, max_len, start)
                if max_len < r - l + 1:
                    max_len = r - l + 1
                    start = l
                r += 1
                l -= 1
            # even palindrome
            l, r = i, i + 1
            while -1 < l <= r < n and s[l] == s[r]:
                # print(l, r, max_len, start)
                if max_len < r - l + 1:
                    max_len = r - l + 1
                    start = l
                r += 1
                l -= 1


        if max_len == -float('inf'):
            return ""

        return s[start:start+max_len]

                

            
