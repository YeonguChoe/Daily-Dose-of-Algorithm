// Time complexity: O(n)
// Space complexity: O(numRows)

int index_to_line(int index, int numRows)
{
    int size_of_set = 2 * (numRows - 1);
    int refined_index = index % size_of_set;

    if (refined_index < (numRows - 1))
    {
        return refined_index % (numRows - 1);
    }

    if (refined_index == (numRows - 1))
    {
        return refined_index;
    }

    if (refined_index > (numRows - 1))
    {
        return (numRows - 1) - (refined_index % (numRows - 1));
    }
}

string convert(string s, int numRows)
{
    if (numRows <= 1) return s;

    vector<string> rows(numRows);
    int n = s.size();

    for (int i = 0; i < n; ++i)
    {
        int line = index_to_line(i, numRows);
        rows[line] += s[i];
    }

    string result;
    for (string& row : rows)
    {
        result += row;
    }
    return result;
}
