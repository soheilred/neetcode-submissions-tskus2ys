class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        rem = [gas[i] - cost[i] for i in range(n)]
        print(rem)

        for i in range(n):
            if rem[i] >= 0:
                total = 0
                for j in range(n):
                    total += rem[(i + j) % n]
                    if total < 0:
                        break
                if j == n - 1 and total >= 0:
                    return i
        return -1


        