class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)

        seqs = []

        for num in nums:
            if num - 1 not in num_set:
                seq = [num]
                n = num
                while n + 1 in num_set:
                    seq.append(num)
                    n = n + 1
                seqs.append(seq)
        
        return max([len(seq) for seq in seqs])
            


        