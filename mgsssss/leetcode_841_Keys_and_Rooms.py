'''
https://leetcode.com/problems/keys-and-rooms/
2024-08-25

이건 생각보다 쉬운 문제
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_list = [False] * len(rooms)
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            rooms_list[i] = True
            for room in rooms[i]:
                dfs(room)

        dfs(0)
        return False if False in rooms_list else True
        