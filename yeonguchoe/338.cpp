// Without memoization
vector<int> countBits(int n)
{
    vector<int> result;
    for (int current_n = 0; current_n <= n; current_n++)
    {
        int copy_current_n = current_n;
        int counter = 0;
        while (copy_current_n > 0)
        {
            if (copy_current_n % 2 == 1)
            {
                counter++;
            }
            copy_current_n /= 2;
        }
        result.push_back(counter);
    }
    return result;
}

// With memoization
vector<int> countBits(int n)
{
    vector<int> memo = {0};

    for (int i = 1; i <= n; i++)
    {
        int new_count = (i % 2) + memo[(i / 2)];
        memo.push_back(new_count);
    }
    return memo;
}
