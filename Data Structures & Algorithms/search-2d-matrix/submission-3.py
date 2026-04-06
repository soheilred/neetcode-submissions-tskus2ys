class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while top <= bot:
            m = top + (bot - top) // 2
            # print(top, m, bot, matrix[m])
            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bot = m - 1
            else:
                break
        
        # top now is the row with the elements including target
        print(top, m, bot)
        top = (bot + top) // 2
        print(matrix[m])
        while l <= r:
            m = l + (r - l) // 2
            if matrix[top][m] < target:
                l = m + 1
            elif matrix[top][m] > target:
                r = m - 1
            else:
                return True
        
        return False
        