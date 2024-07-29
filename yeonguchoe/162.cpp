// Time complexity: O(log n)
// Space complexity: O(log n)이 최대 콜 스택의 개수
int binary_search(vector<int>& nums, int left, int right)
{
    // 최종 시나리오
    if (left == right)
    {
        return left;
    }
    else
    {
        // 중간 값을 구함
        int mid = (left + right) / 2;
        // 1. mid가 상승하고 있는 기울기에 있는 경우
        if (nums[mid] < nums[mid + 1])
        {
            // mid+1을 left로 설정후 binary search 호출
            return binary_search(nums, mid + 1, right);
        }
        // 2. mid가 하강하고 있는 기울기에 있는 경우
        else
        {
            // mid를 right으로 설정후 binary search 호출
            return binary_search(nums, left, mid);
        }
    }
}

int findPeakElement(vector<int>& nums)
{
    return binary_search(nums, 0, nums.size() - 1);
}
