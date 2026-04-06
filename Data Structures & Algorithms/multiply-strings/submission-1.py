class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        n1, n2 = len(num1), len(num2)
        num2 = sum([10 ** (n2 - i - 1) * (ord(num2[i]) - ord('0')) for i in range(len(num2))])
        num1 = sum([10 ** (n1 - i - 1) * (ord(num1[i]) - ord('0')) for i in range(len(num1))])
        print(num1, num2)
        return str(num1 * num2)
        # print(num2)
        # for i in range(len(num1)):
            # res += 10 ** i * (ord(num1[i]) - ord('0'))
        