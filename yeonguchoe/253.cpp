// Time complexity: O(n log n)
// Space complexity: O(n)

int minMeetingRooms(vector<vector<int>>& intervals)
{
    priority_queue<int, vector<int>, greater<int>> min_heap;
    sort(intervals.begin(), intervals.end());
    min_heap.push(intervals[0][1]);

    int max_room = min_heap.size();

    for (int i = 1; i < intervals.size(); i++)
    {
        int earliest_end_time = min_heap.top();
        if (intervals[i][0] >= earliest_end_time)
        {
            min_heap.pop();
            min_heap.push(intervals[i][1]);
        }
        else
        {
            min_heap.push(intervals[i][1]);
        }
        max_room = max(max_room, static_cast<int>(min_heap.size()));
    }
    return max_room;
}
