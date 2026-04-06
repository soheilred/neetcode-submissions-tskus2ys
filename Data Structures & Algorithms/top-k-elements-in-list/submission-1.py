class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # count = sorted(count.items(), key=lambda x: -x[1])
        # return [count[i][0] for i in range(k)]
        buck = defaultdict(list)
        for c in count:
            buck[count[c]].append(c)
        
        print(buck)
        buck = sorted(buck.items(), key=lambda x: -x[0])
        out = []
        for b in buck:
            out.extend(b[1])
            if len(out) >= k:
                return out
        return out
        