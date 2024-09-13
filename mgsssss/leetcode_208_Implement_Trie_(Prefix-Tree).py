'''
https://leetcode.com/problems/implement-trie-prefix-tree/
2024-09-13

처음 풀어보는 유형의 문제 trie 라는 개념을 공부 할 수 있어서 좋았다.
사실 hash 자료구조를 사용하는데, 코드를 구현하면서 개념을 이해할 수 있었다.
'''

class Node:
    def __init__(self, ending=False):
        self.store = {}
        self.ending = ending

class Trie:

    def __init__(self):
        self.root = Node(ending=True)

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.store:
                node.store[ch] = Node()
            node = node.store[ch]
        node.ending = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.store:
                return False
            node = node.store[ch]
        return node.ending

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.store:
                return False
            node = node.store[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)