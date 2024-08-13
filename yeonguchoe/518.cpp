// Time complexity: O(코인수 * 목표금액)
// Space complexity: O(코인수 * 목표금액)

int change(int amount, vector<int>& coins) {
    int num_coin = coins.size();

    // 2D 행렬 만들기
    // 각 cell은 row 아래의 동전들로 해당 column의 금액을 만들수 있는 경우의
    // 수를 의미
    vector<vector<int>> matrix(num_coin + 1, vector<int>(amount + 1, 0));
    // 첫번째 column 1로 초기화
    for (int i = 0; i < num_coin; i++) {
        matrix[i][0] = 1;
    }

    for (int coin_lower_bound = num_coin - 1; coin_lower_bound >= 0;
         coin_lower_bound--) {
        for (int goal_amount = 1; goal_amount <= amount; goal_amount++) {
            if (goal_amount < coins[coin_lower_bound]) {
                matrix[coin_lower_bound][goal_amount] =
                    matrix[coin_lower_bound + 1][goal_amount];
            } else {
                matrix[coin_lower_bound][goal_amount] =
                    matrix[coin_lower_bound]
                          [goal_amount - coins[coin_lower_bound]] +
                    matrix[coin_lower_bound + 1][goal_amount];
            }
        }
    }
    return matrix[0][amount];
}
