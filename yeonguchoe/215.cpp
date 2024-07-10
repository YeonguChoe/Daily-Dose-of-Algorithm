// Time Complexity: O(n log n)
// Space Complexity: O(n)
int findKthLargest(vector<int>& nums, int k)
{
    priority_queue<int, vector<int>, greater<int>> min_heap;

    for (int num : nums)
    {
        min_heap.push(num);
        if (min_heap.size() > k)
        {
            min_heap.pop();
        }
    }
    return min_heap.top();
}
