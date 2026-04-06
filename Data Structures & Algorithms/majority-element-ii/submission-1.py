class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        count = Counter(nums)
        return [i for i in count if count[i] > N // 3]
        