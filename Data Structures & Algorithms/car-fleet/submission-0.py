class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        cars = [(position[i], i, (target - position[i]) / speed[i]) for i in range(n)]
        cars.sort(key=lambda x:-x[0])
        cur_end = 0
        fleets = 0
        print(cars)

        for c in cars:
            if c[2] > cur_end:
                fleets += 1
                cur_end = c[2]
        return fleets
        


'''
x_t = p + v * t

t = ( x_t - p ) / v

--------
[3, 3]

[3, 4.5, 10, 3]
[(4, 0), (1, 1), (0, 2), (7, 3)]
[(7, 3, 3), (4, 0, 3), (1, 1, 4.5), (0, 2, 10)]
res.append()
'''