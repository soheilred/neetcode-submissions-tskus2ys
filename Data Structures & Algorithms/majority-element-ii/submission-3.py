class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # N = len(nums)
        # count = Counter(nums)
        # return [i for i in count if count[i] > N // 3]
        val1, count1 = -9999, 0
        val2, count2 = -9999, 0

        N = len(nums)
        res = []

        for n in nums:
            if val1 == n:
                count1 += 1
            
            elif val2 == n:
                count2 += 1
            
            else:

                if count1 < 1:
                    val1 = n
                    count1 = 1
        
                elif count2 < 1:
                    val2 = n
                    count2 = 1

                else:
                    count1 -= 1
                    count2 -= 1

        count1 = count2 = 0
        for n in nums:
            if val1 == n:
                count1 += 1

            elif val2 == n:
                count2 += 1
        
        if count1 > N // 3:
            res.append(val1)
            
        if count2 > N // 3:
            res.append(val2)
        
        return res