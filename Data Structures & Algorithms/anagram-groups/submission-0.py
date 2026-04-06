class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            k = list(s)
            k.sort()
            d[''.join(k)].append(s)
        return [d[elem] for elem in d]
        