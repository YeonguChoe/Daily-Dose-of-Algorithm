class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # TC: O(n^2) MC: O(1)
        while True:
            # sort the list in reverse order
            stones = sorted(stones, reverse=True)
            if len(stones) == 0:
                # no stones left
                return 0
            elif len(stones) == 1:
                # return the weight of the last remaining stone
                return stones[0]
            y = stones.pop(0) # get the heaviest
            x = stones.pop(0) # second heaviest
            if x != y:
                y = y-x
                stones.append(y)
