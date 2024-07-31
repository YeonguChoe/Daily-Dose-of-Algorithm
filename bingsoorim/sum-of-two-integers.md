## 371. Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the operators + and -.

### Bitwise Operations
For any two numbers, if their binary representations are completely opposite, then XOR operation will directly produce sum of numbers ( in this case carry is 0 ).
If the numbers binary representation is not completely opposite, XOR will only have part of the sum and remaining will be carry, which can be produced by and operation followed by left shift operation.
- For Example 18, 13 => 10010, 01101 => XOR => 11101 => 31 (ans found), and operation => carry => 0
- For Example 7, 5 => steps will be 7|5 => 2|10 => 8|4  => 12|0

```
class Solution:
    def getSum(self, a: int, b: int) -> int:
         # 32 bit mask in hexadecimal
        mask = 0xffffffff 
        while (b & mask > 0):
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a
```
