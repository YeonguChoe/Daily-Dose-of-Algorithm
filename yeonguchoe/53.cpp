// Time complexity: O(n)
// Space complexity: O(1)
int maxSubArray(vector<int> &nums)
{
    int current_max = INT_MIN;
    int current_sum = 0;
    for (int e : nums)
    {
        current_sum += e;
        current_max = max(current_max, current_sum);
        if (current_sum < 0)
        {
            current_sum = 0;
        }
    }
    return current_max;
}
