class TreeNode:
    def __init__(self):
        self.node = [None] * 26
        self.flag = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for w in word:
            i = ord(w) - ord('a')
            if cur.node[i] is None:
                cur.node[i] = TreeNode()
            cur = cur.node[i]
        
        cur.flag = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        n = len(word)
        print(word)

        def dfs(tree, j):
            # print(j)
            if j >= n:
                return tree.flag

            res = False

            if word[j] == '.':
                for i in range(26):
                    if tree.node[i]:
                        res = res or dfs(tree.node[i], j+1)
                return res

            i = ord(word[j]) - ord('a')
            if not tree.node[i]:
                return False

            # cur = cur.node[i]
            return dfs(tree.node[i], j+1)
        
        return dfs(cur, 0)
        
        # return cur.flag

        
        
