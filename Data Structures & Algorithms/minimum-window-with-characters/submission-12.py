class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s_count = Counter(s)
        t_count = Counter(t)
        s_count = defaultdict(int)

        n = len(s)
        # l, r = 0, n - 1
        l = 0
        start = 0
        res = float('inf')

        need, have = len(t_count), 0

        for r in range(n):
            c = s[r]
            s_count[c] += 1

            if c in t_count and t_count[c] == s_count[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < res:
                    res = r - l + 1
                    start = l

                c = s[l] 
                s_count[c] -= 1
                if c in t_count and t_count[c] > s_count[c]:
                    have -= 1
                l += 1
        return s[start:start+res] if res != float('inf') else ''

