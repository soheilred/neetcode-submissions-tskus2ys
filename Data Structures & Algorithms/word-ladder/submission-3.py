class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        seen = set()
        res = float('inf')

        if endWord not in wordList:
            return 0

        def diff(word1, word2):
            count = 0
            n = len(word1)
            for i in range(n):
                if word1[i] != word2[i]:
                    if count < 1:
                        count += 1
                    else:
                        return False
            return True

        def bt(word, cur_ind):
            nonlocal res

            print(word, wordList[cur_ind], res, diff(word, wordList[cur_ind]), diff(word, endWord), seen)
            if diff(word, wordList[cur_ind]) == False:
                return False
            
            if diff(word, endWord):
                res = min(res, len(seen))
                return True

            seen.add(cur_ind)

            for i in range(n):
                if i not in seen:
                    bt(wordList[cur_ind], i)
                    # if bt(wordList[cur_ind], i):
                        # res = min(res, len(seen))
                        # return True
            
            seen.remove(cur_ind)
        
        for i in range(n):
            bt(beginWord, i)

        return res + 2 if 0 <= res < float('inf') else 0

            





        