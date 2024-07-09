Space complexity: O(n)

class KthLargest
{
public:
    priority_queue<int, vector<int>, greater<int>> min_heap;
    int k_value;

    KthLargest(int k, vector<int>& nums)
    {
        k_value = k;
        for (int num : nums)
        {
            min_heap.push(num);
            if (min_heap.size() > k)
            {
                min_heap.pop();
            }
        }
    }

    int add(int val)
    {
        min_heap.push(val);
        while (min_heap.size() > k_value)
        {
            min_heap.pop();
        }
        return min_heap.top();
    }
};
