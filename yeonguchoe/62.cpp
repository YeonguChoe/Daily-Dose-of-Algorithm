// Time complexity: O(mn)
// Memory complexity: O(mn)

int helper(int m, int n, vector<vector<int>>& memo)
{
    int row = m - 1;
    int column = n - 1;

    if (memo[row][column] != -1)
    {
        return memo[row][column];
    }

    if (row == 0 or column == 0)
    {
        memo[row][column] = 1;
        return 1;
    }

    memo[row][column] = helper(m - 1, n, memo) + helper(m, n - 1, memo);

    return memo[row][column];
}

int uniquePaths(int m, int n)
{
    vector<vector<int>> memo1(m, vector<int>(n, -1));
    helper(m, n, memo1);
    return memo1[m - 1][n - 1];
}
