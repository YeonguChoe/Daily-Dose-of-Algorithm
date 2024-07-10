// Time Complexity: O(n^2)
// Space Complexity: O(1)

void rotate(vector<vector<int>>& matrix)
{
    int n = matrix.size();
    // Transpose
    for (int row = 0; row < n; row++)
    {
        for (int column = row + 1; column < n; column++)
        {
            swap(matrix[row][column], matrix[column][row]);
        }
    }

    // Reverse each row
    for (int row = 0; row < n; row++)
    {
        for (int column = 0; column < n / 2; column++)
        {
            swap(matrix[row][column], matrix[row][(n - 1) - column]);
        }
    }
}
