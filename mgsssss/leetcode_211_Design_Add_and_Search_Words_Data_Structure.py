'''
https://leetcode.com/problems/design-add-and-search-words-data-structure/
2024-09-13

208번 문제랑 비슷하게 풀었다. 구조는 비슷한데, 이게 더 생각할 부분이 많았다.
'.' 이부분에 대한 처리가 생각보다 까다로웠다.
'''

class Node:
    def __init__(self, ending=False):
        self.store = {}
        self.ending = ending

class WordDictionary:

    def __init__(self):
        self.root = Node(ending=True)

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.store:
                node.store[ch] = Node()
            node = node.store[ch]
        node.ending = True
        

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.ending
            ch = word[idx]
            if ch in node.store:
                return dfs(node.store[ch], idx + 1)
            if ch == '.':
                if any( dfs(node.store[k], idx+1) for k in node.store ):
                    return True
            return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)