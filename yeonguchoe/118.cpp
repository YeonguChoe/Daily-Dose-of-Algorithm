// Time complexity: O(n^2)
// Space complexity: O(1)

vector<vector<int>> generate(int numRows)
{
    vector<vector<int>> result;
    // 베이스 케이스 1: numRows==1
    result.push_back({1});
    if (numRows == 1)
    {
        return result;
    }
    // 베이스 케이스 1: numRows==2
    result.push_back({1, 1});
    if (numRows == 2)
    {
        return result;
    }


    // 재귀 케이스: numRows>=3
    int i = 3;

    // numRows 개수만큼 반복
    while (i <= numRows)
    {
        vector<int> new_row;
        new_row.push_back(1);

        // 이전 리스트를 가져옴
        vector<int>& previous_row = result[i - 2];

        // 인덱스 1~끝인덱스를 계산해서 새로운 리스트를 만듬
        for (int column = 1; column <= previous_row.size() - 1; column++)
        {
            int new_number = previous_row[column - 1] + previous_row[column];
            new_row.push_back(new_number);
        }
        new_row.push_back(1);
        ++i;
        result.push_back(new_row);
    }

    return result;
}
