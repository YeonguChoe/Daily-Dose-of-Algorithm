'''
https://leetcode.com/problems/number-of-provinces/
2024-08-17
재밌는 문제
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        c_dict = defaultdict(list)
        city = len(isConnected)
        visited = set()
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and i != j:
                    c_dict[i+1].append(j+1)
        for key, val in c_dict.items():
            if key not in visited:
                visited.add(key)
                q = deque([key])
                while q:
                    cur_city = q.popleft()
                    for next_city in c_dict[cur_city]:
                        if next_city not in visited:
                            city -= 1
                            visited.add(next_city)
                            q.append(next_city)

        return city