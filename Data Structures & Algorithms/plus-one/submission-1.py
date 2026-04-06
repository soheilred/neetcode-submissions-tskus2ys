class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)

        for i in range(n - 1, -1, -1):
            tmp = digits[i] + carry
            digits[i] = tmp % 10
            carry = tmp // 10
            if carry == 0:
                return digits
        
        if carry:
            return [carry] + digits
        
        return digits

        