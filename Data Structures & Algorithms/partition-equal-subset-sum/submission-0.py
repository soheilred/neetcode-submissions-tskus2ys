class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def bt(s1, s2, sum1, sum2):
            # print(s1, s2)
            if sum1 == sum2:
                return True

            # for elem in s2:
            k, count = len(s2), 0
            while count < k:
                elem = s2.popleft()
                s1.append(elem)
                if bt(s1, s2, sum1+elem, sum2-elem):
                    return True
                s2.append(s1.pop())
                count += 1
            
            return False
        
        return bt(deque(), deque(nums), 0, sum(nums))
                
            
