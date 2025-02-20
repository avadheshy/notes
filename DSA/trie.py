class TrieNode:
    def __init__(self):
        self.child={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for c in word:
            if c not in node.child:
                node.child[c]=TrieNode()
            node=node.child[c]
        node.is_end=True
    def search(self,word):
        node=self.root
        for c in word:
            if c not in node.child:
                return False
            node=node.child[c]
        return node.is_end


trie = Trie()
arr = ["and", "ant", "do", "geek", "dad", "ball"]
for s in arr:
    trie.insert(s)

# One by one search strings
search_keys = ["do", "gee", "bat","dad"]
for s in search_keys:
    print(f"Key : {s}")
    if trie.search(s):
        print("Present")
    else:
        print("Not Present")