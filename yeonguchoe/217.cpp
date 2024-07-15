// Time complexity: O(n*logn) for n iteration and log n for find operation in set
// Space complexity: O(n) for the set

bool containsDuplicate(vector<int>& nums)
{
    set<int> unique_value;
    for (int i : nums)
    {
        if (unique_value.find(i) != unique_value.end())
        {
            return true;
        }
        unique_value.insert(i);
    }
    return false;
}
