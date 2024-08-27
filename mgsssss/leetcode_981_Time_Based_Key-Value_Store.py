'''
https://leetcode.com/problems/time-based-key-value-store/description/
2024-08-27

제약 조건을 보면
All the timestamps timestamp of set are strictly increasing.
해당 문구가 있는데, 해당 문구가 중요한 키이다.
'''

class TimeMap:

    def __init__(self):
        self.key = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.key:
            l, r = 0, len(self.key[key]) - 1
            while l <= r:
                mid = (l + r) // 2
                if self.key[key][mid][1] <= timestamp:
                    l = mid + 1
                    res = self.key[key][mid][0]
                else:
                    r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)