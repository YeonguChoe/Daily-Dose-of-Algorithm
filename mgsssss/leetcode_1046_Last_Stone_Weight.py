'''
https://leetcode.com/problems/last-stone-weight/
2024-07-15

python 의 heap 자료구조를 활용하여 풀었다.
heaq을 사용한 이유는 지속적으로 최대값에 대한 정렬이 필요해서 이다.
기본적으로 heap 자료구조는 최소값으로 정렬 되지만
tuple을 활용한 트릭을 사용하여, 최대값부터 저장될 수 있도록 하였고,
while 안에 if 를 하나만 넣은것은 어짜피 first 와 second 의 값이 같을 경우는 pop 을 해서 사라지기 때문에
따로 연산할 필요가 없어서 이다.
'''

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1:
            return stones[0]

        hq = []
        for stone in stones:
            heapq.heappush(hq, (-stone, stone))

        while len(hq) != 0:
            if len(hq) == 1:
                return heapq.heappop(hq)[1]
            first = heapq.heappop(hq)[1]
            second = heapq.heappop(hq)[1]
            if first > second:
                val = first - second
                heapq.heappush(hq, (-val, val))
        return 0