class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {}
        for i, num in enumerate(nums):
            if target - num in n_dict:
                return [n_dict[target - num], i]
            n_dict[num] = i
