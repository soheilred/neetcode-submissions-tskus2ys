class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def find_pivot():
            l, r = 0, n - 1
            m = 0
        
            while l <= r:
                m = l + (r - l) // 2
                print(l, m, r)
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            return m
        
        def bst(l, r):
            while l <= r:
                m = l + (r - l) // 2
                print(l, m, r)
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return m
        
        pivot = find_pivot()
        l, r = 0, n - 1

        if target > nums[-1]:
            r = pivot
        else:
            l = pivot
        
        print("here", l, r, pivot)

        res = bst(l, r)
        print(res)
        if nums[res] == target:
            return res
        return -1
        