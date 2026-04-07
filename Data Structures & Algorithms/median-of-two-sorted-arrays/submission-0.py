class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        mid = n // 2
        # if m > n:
            # nums1, nums2 = nums2, nums1

        def get_kth(k):
            l1 = l2 = 0
            
            while True:
                # print(l1, l2, k)
                if l1 == n1:
                    return nums2[l2+k]

                elif l2 == n2:
                    return nums1[l1+k]
                
                if k == 0:
                    return min(nums1[l1+k], nums2[l2+k])
            
                step = max(k // 2, 1)
                i1 = min(l1 + step, n1) - 1 # why -1?
                i2 = min(l2 + step, n2) - 1

                if nums1[i1] < nums2[i2]:
                    k -= (i1 - l1 + 1)
                    l1 = i1 + 1
                
                else:
                    k -= (i2 - l2 + 1)
                    l2 = i2 + 1

            
        
        if n % 2 == 0:
            med1, med2 = get_kth(mid-1), get_kth(mid)
            return (med1 + med2) / 2.

        else:
            return get_kth(mid)

    
'''
nums1=[2,3,5,6]
             m1
nums2=[4,6,7,8,9]
           m2
[2,3,4,5,6,6,7,8,9] med=6 (5th)
m1
m2
med -= (m - l + 1)
m1 elements in nums1 is smaller than m2
l1 = m1 + 1

r1 = m1 - 1
'''