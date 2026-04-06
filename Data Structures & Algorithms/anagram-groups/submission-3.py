class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            count = Counter(s)
            k = [str(count[chr(97 + i)]) for i in range(26)]
            print(k)
            d['.'.join(k)].append(s)
        return [d[elem] for elem in d]
        