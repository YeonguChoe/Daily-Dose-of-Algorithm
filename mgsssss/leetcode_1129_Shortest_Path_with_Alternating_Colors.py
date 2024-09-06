'''
https://leetcode.com/problems/shortest-path-with-alternating-colors/
2024-08-26

쉬워보였는데 생각보다 까다로운 문제.
그런데 풀고나니 쉬워보인다
'''

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [9999] * n
        res[0] = 0
        red_dict = defaultdict(list)
        blue_dict = defaultdict(list)

        for a, b in redEdges:
            red_dict[a].append(b)
        for a, b in blueEdges:
            blue_dict[a].append(b)

        def bfs():
            visited = set()
            q = deque([(0, 0, 'None')])
            while q:
                cur_node, cur_path, cur_color = q.popleft()
                res[cur_node] = min(res[cur_node], cur_path)
                if cur_color != 'b':
                    if cur_node in blue_dict:
                        for next_node in blue_dict[cur_node]:
                            if (next_node, 'b') not in visited:
                                visited.add((next_node, 'b'))
                                q.append((next_node, cur_path+1, 'b'))
                                
                if cur_color != 'r':
                    if cur_node in red_dict:
                        for next_node in red_dict[cur_node]:
                            if (next_node, 'r') not in visited:
                                visited.add((next_node, 'r'))
                                q.append((next_node, cur_path+1, 'r'))

        bfs()
        for i in range(len(res)):
            if res[i] == 9999:
                res[i] = -1
        return res