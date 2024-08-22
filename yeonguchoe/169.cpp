// Time complexity: O(n log n)
// Space complexity: O (1)
int majorityElement(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    return nums[nums.size() / 2];
}
