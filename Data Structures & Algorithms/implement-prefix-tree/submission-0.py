class TreeNode:
    def __init__(self):
        self.node = [None] * 26
        self.flag = False

class PrefixTree:

    def __init__(self):
        self.tree = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.tree

        for w in word:
            ind = ord(w) - ord('a')
            if cur.node[ind] == None:
                cur.node[ind] = TreeNode()
            cur = cur.node[ind]
        
        cur.flag = True


    def search(self, word: str) -> bool:
        cur = self.tree

        for w in word:
            ind = ord(w) - ord('a')
            if cur.node[ind] == None:
                return False
            cur = cur.node[ind]
        return cur.flag
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.tree

        for w in prefix:
            ind = ord(w) - ord('a')
            if cur.node[ind] == None:
                return False
            cur = cur.node[ind]
        return True
        