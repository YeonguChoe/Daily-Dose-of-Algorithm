## 338. Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of I.

### Brute Force 
Simply convert each number to a binary string, and count the number of 1's in the resulting string. This will have time complexity of O(n * number of digits).
> **_NOTE_**: The bin() method returns:
> the binary string equivalent to the given integer, 
> or TypeError for a non-integer argument

```
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(bin(i).count('1'))
        return res
```

### Binary solution
Remember the following two points:
- All whole numbers can be represented by 2N (even) and 2N+1 (odd)
- For a given binary number, multiplying by 2 is the same as adding a zero at the end (just like we are adding a 0 when multiplying by 10 in base 10)

Since multiplying by 2 just adds a zero, then any number and its double will have the same number of 1's. 
Therefore, we can see that any number will have the same bit count as half that number, with an extra 1, if it's an odd number. 
We iterate through the range of numbers and calculate each bit count successively in this manner:
```
class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0] # define the base case
        for i in range(1, n+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
```
#### Time and Space Complexity
- Time: O(n) - iterates through the range of numbers once
- Space: O(n) - uses a n-sized array
