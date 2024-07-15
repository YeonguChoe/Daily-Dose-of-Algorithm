// Time complexity: O(lg n)
// Space complexity: O(1)

int findMin(vector<int>& nums)
{
    int left = 0;
    int right = nums.size() - 1;
    int first_value = nums[0];

    if (nums[left] <= nums[right])
    {
        return nums[0];
    }

    while (left <= right)
    {
        int middle = (left + right) / 2;

        if (nums[middle] < first_value)
        {
            if (nums[middle] < nums[middle - 1])
            {
                return nums[middle];
            }
            else
            {
                right = middle - 1;
            }
        }
        else
        {
            left = middle + 1;
        }
    }
    return 0;
}
