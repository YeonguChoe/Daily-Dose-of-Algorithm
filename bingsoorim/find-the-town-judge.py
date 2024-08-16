class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # using two hashmaps --> this can be improved by just using one hashmap
        incoming = defaultdict(int) # n-1
        outgoing = defaultdict(int) # 0

        for src, dst in trust:
            outgoing[src] += 1
            incoming[dst] += 1

        # go through every single node
        for i in range(1, n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i
        return -1
