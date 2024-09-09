class Solution {
public:
    // 일반적인 2D 행렬에서의 DFS
    void dfs(vector<vector<char>>& grid, int cur_row, int cur_column) {

        if (cur_row < 0 or cur_row >= grid.size() or cur_column < 0 or
            cur_column >= grid[0].size()) {
            return;
        }

        if (grid[cur_row][cur_column] == 'X' or
            grid[cur_row][cur_column] == 'T') {
            return;
        }
        grid[cur_row][cur_column] = 'T'; // 임시표시

        dfs(grid, cur_row - 1, cur_column);
        dfs(grid, cur_row + 1, cur_column);
        dfs(grid, cur_row, cur_column - 1);
        dfs(grid, cur_row, cur_column + 1);
    }

    void solve(vector<vector<char>>& board) {
        int row = board.size();
        int column = board[0].size();

        // 양쪽 세로
        for (int i = 0; i < row; i++) {
            if (board[i][column - 1] == 'O') {
                dfs(board, i, column - 1);
            }
            if (board[i][0] == 'O') {
                dfs(board, i, 0);
            }
        }

        // 위 아래 가로
        for (int i = 0; i < column; i++) {
            if (board[0][i] == 'O') {
                dfs(board, 0, i);
            }
            if (board[row - 1][i] == 'O') {
                dfs(board, row - 1, i);
            }
        }

        // 전체 board를 돌면서
        // 1) T -> O 로 바꿈
        // 2) O -> X 로 바꿈 (X로 둘러쌓여 있는것)
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                if (board[i][j] == 'T') {
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
    }
};
