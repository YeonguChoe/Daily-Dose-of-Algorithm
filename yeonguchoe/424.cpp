// Time complexity: O(n)
// Space complexity: O(1)


int characterReplacement(string s, int k)
{
    int arr[26] = {};
    int left = 0;
    int right = 0;
    int res = 0;

    while (right < static_cast<int>(s.length()))
    {
        char right_selected = tolower(s[right]) - 97;
        arr[right_selected] += 1;

        int frequent_alphabet = *max_element(arr, arr + 26);

        while (right - left + 1 - frequent_alphabet > k)
        {
            char left_selected = tolower(s[left]) - 97;
            arr[left_selected] -= 1;
            left++;
        }
        res = max(res, right - left + 1);
        right++;
    }
    return res;
}
