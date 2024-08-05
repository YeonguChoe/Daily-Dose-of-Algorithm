// Time complexity: O(n)
// Space complexity: O(n)
int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat)
{
    // 1. arr의 index를 mat의 좌표값으로 변환해주는 map 만들기
    // 키: 인덱스, 값: 좌표 [x,y]
    unordered_map<int, array<int, 2>> number_to_coordinate;

    int row_count = mat.size();
    int column_count = mat[0].size();

    for (int r = 1; r <= row_count; r++)
    {
        for (int c = 1; c <= column_count; c++)
        {
            number_to_coordinate[mat[r - 1][c - 1]] = array<int, 2>{r, c};
        }
    }

    // 2. 키: row번호, 값: 해당 row에 칠해진 cell의 개수
    unordered_map<int, int> painted_cells_in_specific_row;
    // 3. 키: column번호, 값: 해당 column에 칠해진 cell의 개수
    unordered_map<int, int> painted_cells_in_specific_column;

    // 4. arr의 각 element를 돌면서 위의 맵을 갱신
    for (int i = 0; i < arr.size(); i++)
    {
        array<int, 2> cell_coordinate = number_to_coordinate[arr[i]];
        int row_of_selected_cell = cell_coordinate[0];
        int column_of_selected_cell = cell_coordinate[1];
        painted_cells_in_specific_row[row_of_selected_cell] += 1;
        painted_cells_in_specific_column[column_of_selected_cell] += 1;

        // 만약에 특정 row나 column이 다 칠해져 있으면 현재 index 반환
        if (painted_cells_in_specific_row[row_of_selected_cell] >=
            column_count or
            painted_cells_in_specific_column[column_of_selected_cell] >=
            row_count)
        {
            return i;
        }
    }
    // 못찾았으면 input 문제가 잘못 되었으므로 -1 반환
    return -1;
}
