vector<int> twoSum(vector<int>& nums, int target)
{
    unordered_map<int, int> kv;
    for (int i = 0; i < nums.size(); i++)
    {
        kv[nums[i]] = i;
    }
    for (int i = 0; i < nums.size(); i++)
    {
        if (kv.find(target - nums[i]) != kv.end() &&
            kv[target - nums[i]] != i)
        {
            return {i, kv[target - nums[i]]};
        }
    }
    return {};
}
