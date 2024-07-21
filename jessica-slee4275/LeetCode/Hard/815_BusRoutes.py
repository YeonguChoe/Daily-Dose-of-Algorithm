"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Example 2:
Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

Constraints:
1 <= routes.length <= 500.
1 <= routes[i].length <= 10**5
All the values of routes[i] are unique.
sum(routes[i].length) <= 10**5
0 <= routes[i][j] < 10**6
0 <= source, target < 10**6
"""
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        
        max_stop = max(max(r) for r in routes)
        if max_stop < target or source > max_stop: return -1

        n = len(routes)
        min_buses_to_reach = [float('inf')] * (max_stop+1)
        min_buses_to_reach[source] = 0
        # print(min_buses_to_reach)
        arrived = False
        while not arrived:
            arrived = True
            for r in routes:
                i = float('inf')
                for stop in r:
                    i = min(i, min_buses_to_reach[stop])
                    # print(stop, min_buses_to_reach, min_buses_to_reach[stop], i)
                i += 1
                # print('--------------')
                for stop in r:
                    print(stop, min_buses_to_reach, min_buses_to_reach[stop], i)
                    if min_buses_to_reach[stop] > i:
                        min_buses_to_reach[stop] = i
                        arrived = False
                # print('--------------')
                # print('--------------')
        return min_buses_to_reach[target] if min_buses_to_reach[target] < float('inf') else -1
