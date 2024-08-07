// Time complexity: O(mn)
// Space complexity: O(1)
vector<int> spiralOrder(vector<vector<int>>& matrix)
{
    vector<int> result;
    int num_row = matrix.size();
    int num_column = matrix[0].size();

    int left = 0;
    int up = 0;
    int right = matrix[0].size() - 1;
    int down = matrix.size() - 1;

    while (result.size() < num_row * num_column)
    {
        // 1단계 트랙 1번 돌기
        // 1) left->right
        for (int x = left; x <= right; x++)
        {
            result.push_back(matrix[up][x]);
        }
        // 2) up->down
        for (int y = up + 1; y <= down; y++)
        {
            result.push_back(matrix[y][right]);
        }
        // 3) right->left
        if (up != down) //돌지 않은 row가 더 있는지 체크
        {
            for (int x = right - 1; x >= left; x--)
            {
                result.push_back(matrix[down][x]);
            }
        }
        // 4) down->up
        if (right != left) // 돌지 않은 column이 더 있는지 체크
        {
            for (int y = down - 1; y > up; y--)
            {
                result.push_back(matrix[y][left]);
            }
        }
        // 2단계) 안쪽 트랙으로 이동
        left += 1;
        right -= 1;
        up += 1;
        down -= 1;
    }
    return result;
}
