// Time complexity: O(n log k)
// Space complexity: O(n+k)

vector<int> topKFrequent(vector<int> &nums, int k)
{
    // frequency를 저장하는 map 만들기
    unordered_map<int, int> frequency;
    for (int num : nums)
    {
        frequency[num] += 1;
    }
    // frequency가 낮은 값이 heap에서 위에 위치
    // frequency가 높은 값이 heap에서 아래에 위치
    auto comparator = [&frequency](int a, int b)
    {
        return frequency[a] > frequency[b];
    };
    priority_queue<int, vector<int>, decltype(comparator)> heap(comparator);

    // heap 만들기
    for (auto p : frequency)
    {
        heap.push(p.first);
        if (heap.size() > k)
        {
            heap.pop();
        }
    }

    // 리스트로 만들기
    vector<int> result;
    while (!heap.empty())
    {
        result.push_back(heap.top());
        heap.pop();
    }
    return result;
}
