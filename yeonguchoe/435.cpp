// Time complexity: O(n log n) 가장 빠른 정렬 방법.
// Space complexity: O(log n)
int eraseOverlapIntervals(vector<vector<int>> &intervals)
{
    int removed_cnt = 0;
    int recently_ended_at = INT_MIN;
    sort(intervals.begin(), intervals.end(), comparator);

    for (int i = 0; i < intervals.size(); i++)
    {
        int start = intervals[i][0];
        int end = intervals[i][1];
        if (start < recently_ended_at)
        {
            removed_cnt++;
        }
        else
        {
            recently_ended_at = end;
        }
    }
    return removed_cnt;
}
