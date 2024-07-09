Time complexity: O(1)
Space complexity: O(n)

class MinStack
{
public:
    stack<int> original;
    stack<int> current_min;
    MinStack()
    {
    }

    void push(int val)
    {
        original.push(val);

        if (current_min.empty())
        {
            current_min.push(val);
        }
        else
        {
            current_min.push(min(current_min.top(), val));
        }
    }

    void pop()
    {
        current_min.pop();
        return original.pop();
    }

    int top()
    {
        return original.top();
    }

    int getMin()
    {
        return current_min.top();
    }
};
