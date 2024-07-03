vector<vector<int>> threeSum(vector<int>& nums)
{
    unordered_map<int, int> kv;
    set<vector<int>> s;

    for (int i = 0; i < nums.size(); i++)
    {
        kv[nums[i]] = i;
    }

    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = i + 1; j < nums.size(); j++)
        {
            int complement = -nums[i] - nums[j];
            if (kv[complement] != 0 &&
                kv[complement] != i &&
                kv[complement] != j)
            {
                vector<int> temp = {nums[i], nums[j], complement};
                sort(temp.begin(), temp.end());
                s.insert(temp);
            }
        }
    }
    vector<vector<int>> result(s.begin(), s.end());
    return result;
}
