// Bottom-up 접근법
int coinChange(vector<int>& coins, int amount) {
    // Memoization 배열 선언
    // [0,∞,∞,∞,∞,∞,∞]
    // 인덱스: 돈
    // 엘리먼트: 해당 돈을 만드는데 드는 최소한의 동전 갯수
    int M[amount + 1];
    fill(M, M + amount + 1, INT_MAX);
    M[0] = 0;

    // index 1~amount 까지 채워 넣음.
    for (int i = 1; i <= amount; i++) {
        // 동전의 종류를 하나씩 선택해 가며, 남은 금액에서 빼봄
        for (int c : coins) {
            // 만약에 뺏을때 값이 음수이면 메모아이제이션을 갱신 하지 않음.
            if (i - c >= 0 and M[i - c] < INT_MAX) {
                // 해당 번째 cell의 값을 최소한의 동전 갯수로 업데이트
                M[i] = min(M[i], M[i - c] + 1);
            }
        }
    }
    // amount 값을 만드는데 최소한으로 드는 동전의 개수 반환F
    if (M[amount] != INT_MAX) {
        return M[amount];
    }
    // 만약에 도달할수 없는 돈이면 -1 반환
    return -1;
}
// Time complexity: O(amount * 동전의 종류)
// Space complexity: O(amount)
};
