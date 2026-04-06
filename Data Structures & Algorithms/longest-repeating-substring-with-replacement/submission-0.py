class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {s[0]: 1}
        l, r = 0, 1
        n = len(s)
        max_len = 0
        res = 0

        while r < n:
            count[s[r]] = count.get(s[r], 0) + 1
            max_len = max(max_len, count[s[r]])
            rem = (r - l + 1) - max_len
            while rem > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
                max_len = max(max_len, count[s[l]])
                rem = (r - l + 1) - max_len
            res = max(res, r - l + 1)
            r += 1
        
        return res


        


'''
        l = 0       l = 0
        r = 1       r = 2
counts = {X: 1}     {x: 1, y: 1}
s[l:r]
'''