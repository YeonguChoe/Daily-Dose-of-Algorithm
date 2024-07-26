// Time complexity: O(n)
// Space complexity: O(n)

class BrowserHistory
{
public:
    stack<string> previous_url;
    stack<string> next_url;
    string current_url = "";
    BrowserHistory(string homepage) { current_url = homepage; }

    void visit(string url)
    {
        previous_url.push(current_url);
        while (!next_url.empty())
        {
            next_url.pop();
        }
        current_url = url;
    }

    string back(int steps)
    {
        int refined_step = steps;
        if (steps > previous_url.size())
        {
            refined_step = previous_url.size();
        }

        while (refined_step > 0)
        {
            next_url.push(current_url);
            current_url = previous_url.top();
            previous_url.pop();
            --refined_step;
        }
        return current_url;
    }

    string forward(int steps)
    {
        int refined_step = steps;
        if (steps > next_url.size())
        {
            refined_step = next_url.size();
        }

        while (refined_step > 0)
        {
            previous_url.push(current_url);
            current_url = next_url.top();
            next_url.pop();
            --refined_step;
        }
        return current_url;
    }
};
