## 190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

### Brute Force
Convert int binary -> str -> int binary
> **_NOTE_**: `'{0:032b}'.format(n)` or `f'{n:032b}'` converts to a 32-bit representation of the number in binary.
```
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f'{n:032b}'[::-1], 2)
```
> `int(..., 2)` converts the number back to the appropriate base


### Bit Manipulation
Basically print each bit into its reversed counterpart
```
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # Iterate over all 32 bits of the given number
        for i in range(32):
            if n & 1:
                res += 1 << (31-i)
            n >>= 1
        return res
```

### By Recursion
Some ppl solved this problem by recursion... will come back for it later...
