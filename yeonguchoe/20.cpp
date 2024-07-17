// Time complexity: O(n)
// Space complexity: O(n)

bool isValid(string s)
{
    stack<char> monotonic_stack;
    for (char l : s)
    {
        if (l == '(' || l == '{' || l == '[')
        {
            monotonic_stack.push(l);
        }
        if (l == ')' || l == '}' || l == ']')
        {
            if (monotonic_stack.size() == 0)
            {
                return false;
            }
            if ((monotonic_stack.top() == '(' && l == ')') ||
                (monotonic_stack.top() == '{' && l == '}') ||
                (monotonic_stack.top() == '[' && l == ']'))
            {
                monotonic_stack.pop();
            }
            else
            {
                return false;
            }
        }
    }
    if (!monotonic_stack.empty())
    {
        return false;
    }
    else
    {
        return true;
    }
};
