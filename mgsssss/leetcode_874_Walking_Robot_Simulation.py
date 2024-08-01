'''
https://leetcode.com/problems/walking-robot-simulation/
2024-08-01

문제 그대로 코드로 옮기면 되는 문제,
방향 전환하는거
장애물 처리 하는거
이 두가지만 잘하면 문제는 풀린다.
그리고 장애물은 해시를 사용했다.
'''

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        start = [0, 0]
        delta = {
            'Y' : ['MX','X'],
            'X' : ['Y','MY'],
            'MX' : ['MY','Y'],
            'MY' : ['X','MX'],
        }
        obstacle_dict = {(x, y) for x, y in obstacles }
        delta_index = 'Y'
        res = 0
        for command in commands:
            if command == -1 or command == -2:
                delta_index = delta[delta_index][command]
            else:
                for _ in range(command):
                    if delta_index == 'Y':
                        if (start[0], start[1]+1) in obstacle_dict:
                            break
                        start[1] += 1
                    if delta_index == 'X':
                        if (start[0]+1, start[1]) in obstacle_dict:
                            break                        
                        start[0] += 1
                    if delta_index == 'MX':
                        if (start[0]-1, start[1]) in obstacle_dict:
                            break                        
                        start[0] -= 1
                    if delta_index == 'MY':
                        if (start[0], start[1]-1) in obstacle_dict:
                            break                        
                        start[1] -= 1
            res = max(res, (start[0]*start[0] + start[1]*start[1]))
        return res
                
                
