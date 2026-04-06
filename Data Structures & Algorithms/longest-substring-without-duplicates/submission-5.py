class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        positions = {}
        cur_max = 0
        prev = -1

        for i in range(len(s)):
            print(i, s[i], cur_max)
            if s[i] in positions:
                prev = max(positions[s[i]], prev)
                # positions[s[i]] = i
            # else:
            positions[s[i]] = i
        
            cur_max = max(cur_max, i - prev)

        return cur_max
        