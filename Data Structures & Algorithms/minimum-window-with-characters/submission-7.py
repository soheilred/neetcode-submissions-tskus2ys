class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        count_t = Counter(t)
        count_s = Counter(s[0:m-1])

        if m > n: return ""
        # elif m == n and s == t:
            # return s
        # elif m == n and s != t:
            # return ""
        if n == 0 or m == 0: return ""
        # if count_t == count_s: return s
        # elif count_t > count_s: return ""

        min_len = float('inf')
        l = 0
        start = 0

        for r in range(m-1, n):
            count_s[s[r]] += 1
            # print(count_s)
            while count_s >= count_t:
                # print("in", count_s, min_len, start)
                if min_len > r - l + 1:
                    min_len = r - l + 1
                    start = l
                count_s[s[l]] -= 1
                l += 1
        print(start, min_len)

        if min_len < float('inf'):
            return s[start:start+min_len]

        else:
            # return s[start:]
            return ""

        