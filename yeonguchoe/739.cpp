//  Time Complexity: O(2n): O(n) for push to monotonic stack + O(n) for popping from monotonic stack
// Space complexity: O(n): Maximum stack size can be n

vector<int> dailyTemperatures(vector<int>& temperatures)
{
    vector<int> result(temperatures.size(), 0);
    stack<int> value;
    stack<int> index;
    for (int i = 0; i < temperatures.size(); i++)
    {
        while (!value.empty() && temperatures[i] > value.top())
        {
            int start_day = index.top();
            int end_day = i;
            result.at(start_day) = i - start_day;
            value.pop();
            index.pop();
        }
        value.push(temperatures[i]);
        index.push(i);
    }
    return result;
}
