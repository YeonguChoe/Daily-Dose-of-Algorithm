// Time complexity: O(1)
// Space complexity: O(1)

int getSum(int a, int b) {
    int carry = (a&b)<<1;
    int no_carry = (a^b);

    return carry+no_carry;
}
