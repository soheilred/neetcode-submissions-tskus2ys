class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(s)) + '#' + s for s in strs])

    def decode(self, s: str) -> List[str]:
        print(s)
        strs = []
        i = 0
        while i < len(s):
            num = 0
            if s[i].isdigit():
                j = i + 1
                num += int(s[i])
                while s[j] != '#':
                    num = num * 10 + int(s[j])
                    j += 1

                # pass the '#'
                k = j + 1
                cur_s = ''

                while k < j + 1 + num:
                    cur_s += s[k]
                    k += 1

                i = k
                strs.append(cur_s)
                    
        return strs

