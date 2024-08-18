'''
https://leetcode.com/problems/gas-station/
2024-08-18

코드는 쉽다. But 생각하는 것이 힘들다...
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        tank = 0
        max_len = 0
        for i in range(N*2):
            tank += gas[i%N] - cost[i%N]
            if tank >= 0:
                max_len += 1
            else:
                max_len = 0
            tank = max(tank, 0)
        
        return (N * 2) - max_len if max_len >= N else -1

        '''
        N = len(gas)
        for i in range(N):
            tank = 0
            for j in range(N):
                tank += gas[(i+j)%N]
                tank -= cost[(i+j)%N]
                if tank < 0:
                    break
                if j == N - 1:
                    return i
        return -1
        '''
