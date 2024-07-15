'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
2024-07-15

사실 문제가 조금 이해 되지 않았다.
return min(nums) -> 이렇게 해도 문제가 풀렸다.
그런데 문제에서 원하는 방식으로 룰어주는게 예의 같아서

고민해보니 nums의 첫번째 인덱스와 마지막 인덱스의 크기를 비교해서
첫번째 인덱스가 마지막 인덱스의 크기보다 작다면 제대로 정렬된거라고 생각했다.
그래서 무한루프를 만들어서 거기 안에서 q 를 한칸씩 rotate 시켜주면서 하니 성능도 좋게나왔다.

'''

from collections import deque

class Solution:
    def findMin(self, nums: List[int]) -> int:
        q = deque(nums)
        if len(nums) == 1:
            return nums[0]
        while q:
            q.rotate(1)
            if q[0] < q[-1]:
                return q[0]