class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        num_max = 0
        max_count = float('-inf')

        for c in count:
            if max_count < count[c]:
                num_max = 1
                max_count = count[c]
            
            elif max_count == count[c]:
                num_max += 1
        
        print(num_max, max_count)
        
        return max((n + 1) * (max_count - 1) + num_max, len(tasks))

        