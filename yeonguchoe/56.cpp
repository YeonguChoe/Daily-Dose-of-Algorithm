// Time complexity: O(n log n)
// Space complexity: O(n)

vector<vector<int>> merge(vector<vector<int>>& intervals)
{
    sort(intervals.begin(), intervals.end());

    vector<vector<int>> result;

    vector<int> selected = intervals[0];
    for (int i = 1; i < intervals.size(); i++)
    {
        if (intervals[i][0] <= selected[1])
        {
            if (intervals[i][1] < selected[1])
            {
                continue;
            }
            selected[1] = intervals[i][1];
        }
        else
        {
            result.push_back(selected);
            selected = intervals[i];
        }
    }
    result.push_back(selected);
    return result;
}
