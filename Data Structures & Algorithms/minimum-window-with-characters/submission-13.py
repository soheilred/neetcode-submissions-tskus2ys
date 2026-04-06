class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)
        t_count = Counter(t)
        s_count = defaultdict(int)
        t_set = set(t)
        l = 0
        min_len = float('inf')
        need = len(t_set)

        for r in range(N):
            if s[r] in t_count:
                s_count[s[r]] += 1

                if t_count[s[r]] == s_count[s[r]] and s[r] in t_set:
                    # need -= 1
                    t_set.remove(s[r])
            
            # if t_count becomes empty, aka, all the characters have been seen
            # while need == 0:

            while len(t_set) == 0:
                # print(l, r, min_len)
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    # need += 1
                    if s_count[s[l]] < t_count[s[l]]:
                        t_set.add(s[l])

                l += 1
        
        return s[start:start+min_len] if min_len < float('inf') else ''
'''
s = "OUZODYXAZV", t = "XYZ"
how to trigger the left pointer to proceed?
- all of the counts have been met, let's keep track of this using an integer

'''
        # n, m = len(s), len(t)

        # if m > n: return ""
        # if n == 0 or m == 0: return ""

        # count_t = Counter(t)
        # count_s = Counter(s[0:m-1])

        # min_len = float('inf')
        # l = 0
        # start = 0

        # for r in range(m-1, n):
        #     count_s[s[r]] += 1
        #     # print(count_s)
        #     while count_s >= count_t:
        #         # print("in", count_s, min_len, start)
        #         if min_len > r - l + 1:
        #             min_len = r - l + 1
        #             start = l
        #         count_s[s[l]] -= 1
        #         l += 1
        # print(start, min_len)

        # if min_len < float('inf'):
        #     return s[start:start+min_len]

        # else:
        #     # return s[start:]
        #     return ""

        