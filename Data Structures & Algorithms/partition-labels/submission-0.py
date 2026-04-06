class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)

        pos = {}

        for i, c in enumerate(s):
            if c not in pos:
                pos[c] = [i, i]
            else:
                pos[c][1] = i
        print(pos)

        # merge when there's an intersection
        res = []
        start, end = pos[s[0]]

        for c in pos:
            s, e = pos[c]
            if s < end:
                end = max(end, e)
                start = min(start, s)

            if e > end:
                res.append(end - start + 1)
                end = e
                start = s
        res.append(end-start+1)
        return res
            