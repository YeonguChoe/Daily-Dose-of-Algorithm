class Solution
{
public:
    priority_queue<int> max_heap;

    int lastStoneWeight(vector<int>& stones)
    {
        for (int stone : stones)
        {
            max_heap.push(stone);
        }
        while (max_heap.size() > 1)
        {
            int larger = max_heap.top();
            max_heap.pop();
            int smaller = max_heap.top();
            max_heap.pop();
            if (larger > smaller)
            {
                int new_stone = larger - smaller;
                max_heap.push(new_stone);
            }
        }
        max_heap.push(0);
        return max_heap.top();
    }
};
