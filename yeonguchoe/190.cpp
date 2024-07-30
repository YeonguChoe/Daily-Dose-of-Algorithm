// Time complexity: O(1)
// Space complexity: O(1)

int reverseBits(uint32_t n)
{
    int result = 0;
    for (int i = 0; i < 32; i++)
    {
        int last_bit = n % 2;
        int new_number = last_bit << (31 - i);
        result += new_number;
        n /= 2;
    }
    return result;
}
