A Trie (also known as a prefix tree) is a tree data structure used for efficient retrieval of strings, especially useful for tasks like autocomplete and spell checking.

# Key Concepts of a Trie
Each node represents a character.

Each path from the root to a leaf represents a word or a prefix.

Nodes store a dictionary of children and a flag indicating if the node completes a word.


```
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
```
# Easy-Level Trie Questions
| # | Title                            | LeetCode Link                                                                        |
| - | -------------------------------- | ------------------------------------------------------------------------------------ |
| 1 | **Implement Trie (Prefix Tree)** | [🔗 208. Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/)  |
| 2 | **Longest Common Prefix**        | [🔗 14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) |
| 3 | **Replace Words**                | [🔗 648. Replace Words](https://leetcode.com/problems/replace-words/)                |

---
 # Medium-Level Trie Questions

 | # | Title                                           | LeetCode Link                                                                                                 |
| - | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 4 | **Add and Search Word - Data structure design** | [🔗 211. Add and Search Word](https://leetcode.com/problems/add-and-search-word-data-structure-design/)       |
| 5 | **Design Search Autocomplete System**           | [🔗 642. Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) |
| 6 | **Word Search II**                              | [🔗 212. Word Search II](https://leetcode.com/problems/word-search-ii/)                                       |
| 7 | **Prefix and Suffix Search**                    | [🔗 745. Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)                   |
| 8 | **Stream of Characters**                        | [🔗 1032. Stream of Characters](https://leetcode.com/problems/stream-of-characters/)                          |
| 9 | **Search Suggestions System**                   | [🔗 1268. Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)                |

---
 # Hard-Level Trie Questions

 | #  | Title                                      | LeetCode Link                                                                                               |
| -- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| 10 | **Palindrome Pairs**                       | [🔗 336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)                                 |
| 11 | **Concatenated Words**                     | [🔗 472. Concatenated Words](https://leetcode.com/problems/concatenated-words/)                             |
| 12 | **Maximum XOR of Two Numbers in an Array** | [🔗 421. Maximum XOR of Two Numbers](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) |
