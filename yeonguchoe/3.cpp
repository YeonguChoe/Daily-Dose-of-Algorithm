// Time complexity: O(n)
// Space complexity: O(n)

int lengthOfLongestSubstring(string s)
{
    unordered_map<char, int> kv;
    int left = 0;
    int right = 0;
    int res = 0;

    int size = s.length();

    while (right < size)
    {
        kv[s[right]]++;

        while (kv[s[right]] > 1)
        {
            kv[s[left]]--;
            left++;
        }

        int window_size = right + 1 - left;
        if (window_size > res)
        {
            res = window_size;
        }
        right++;
    }
    return res;
}
