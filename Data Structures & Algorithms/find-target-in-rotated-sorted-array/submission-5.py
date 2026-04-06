class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        m = (r - l) // 2

        def bst(arr, offset):
            l, r = 0, len(arr) - 1

            while l <= r:
                m = l + (r - l) // 2
                print(l, m, r, nums[m+offset])
                if nums[offset+m] < target:
                    l = m + 1

                elif nums[offset+m] > target:
                    r = m - 1

                else:
                    return m + offset

            return -1

        while l < r:
            m = l + (r - l) // 2
            # the breaking point is on the right of the tree
            if  nums[m] > nums[r]:
                l = m + 1
            
            elif nums[m] < nums[r]:
                r = m
        
        # bp = ( l + r ) // 2
        print(l, m, r)
        print(nums[:l], nums[l:])
        left = bst(nums[:l], 0)
        right = bst(nums[l:], l) 
        print(left, right)
        if left == right == -1:
            return -1
        return left if left != -1 else right
