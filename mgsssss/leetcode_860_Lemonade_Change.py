'''
https://leetcode.com/problems/lemonade-change/
2024-08-16

코딩하면서 안풀릴거 같았는데 풀렸다.
하라는대로만 하면 되는 문제
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_dict = {
            5 : 0,
            10 : 0,
            20 : 0
        }
        total = 0
        for bill in bills:
            change_dict[bill] += 1
            change = bill - 5
            if change == 0:
                pass
            elif change in change_dict:
                if change_dict[change] > 0:
                    change_dict[change] -= 1
                else:
                    return False
            elif change_dict[10] > 0 and change_dict[5] > 0:
                change_dict[10] -= 1
                change_dict[5] -= 1
            elif change_dict[5] >= 3:
                change_dict[5] -= 3
            else:
                return False
        return True

                