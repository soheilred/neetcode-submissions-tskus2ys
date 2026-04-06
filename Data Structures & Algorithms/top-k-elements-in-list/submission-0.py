class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = sorted(count.items(), key=lambda x: -x[1])
        print(count)
        return [count[i][0] for i in range(k)]
        