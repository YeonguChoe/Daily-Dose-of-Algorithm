// Time complexity: O(2^n)
// Space complexity: O(n)

void backtrack(vector<string>& result, string current_string, int left_cnt,
               int right_cnt, int n)
{
    if (current_string.size() == 2 * n)
    {
        result.push_back(current_string);
        return;
    }

    if (left_cnt < n)
    {
        current_string += '(';
        backtrack(result, current_string, left_cnt + 1, right_cnt, n);
        current_string.pop_back();
    }

    if (left_cnt > right_cnt)
    {
        current_string += ')';
        backtrack(result, current_string, left_cnt, right_cnt + 1, n);
        current_string.pop_back();
    }
}
