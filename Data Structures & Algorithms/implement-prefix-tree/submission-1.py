class TrieNode():
    def __init__(self, children={}, is_end=False):
        self.children = children
        self.is_end = is_end
class PrefixTree:
    def __init__(self):
        self.root = TrieNode({}, False)

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                # set a new node
                curr.children[c] = TrieNode({}, False)
            # move to another node
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            # move to another TrieNode
            curr = curr.children[c]
        
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True
        
        