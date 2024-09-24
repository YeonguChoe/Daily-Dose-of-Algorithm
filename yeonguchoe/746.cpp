// 문제 설명: cost 배열은 해당 계단에서 움직일때 드는 돈의 값을 가지고 있음.

// Top Down
// 맨 꼭데기 부터 고려함.
int minCostClimbingStairs(vector<int> &cost)
{
    // memo 배열 선언
    // [∞,∞,∞,∞,∞,∞,∞]
    // 인덱스: 계단의 번째
    // element: 해당 인덱스 번째 계단에 도달하는데 소요되는 최소 돈
    int memo[cost.size() + 1];
    fill(memo, memo + cost.size() + 1, INT_MAX);
    return minCostToReach(cost.size(), cost, memo);
}

int minCostToReach(int step, vector<int> &cost, int *M)
{
    // 만약에 0번째 또는 1번째 계단에 도달했으면, 도착한거임.
    // 왜냐하면, 처음에 0번째 또는 1번째 계단에서 시작 가능.
    if (step <= 1)
    {
        return 0;
    }

    // Memo 배열에서 값을 가져옴.
    // 2 계단을 아래로 내려올때, memo에 먼저 들어가게 됨.
    // 1 계단 내려갈때, memo
    if (M[step] != INT_MAX)
    {
        return M[step];
    }

    // 1 계단을 내려갈때와 2 계단을 내려갈때를 계산함.
    int came_from_one_stepdown =
        cost[step - 1] + minCostToReach(step - 1, cost, M);
    int came_from_two_stepdown =
        cost[step - 2] + minCostToReach(step - 2, cost, M);

    // 1계단 내려갈때 케이스와 2계단 내려갈때 케이스
    int min_cost = min(came_from_one_stepdown, came_from_two_stepdown);
    M[step] = min_cost; // memo 테이블에 대입
    return min_cost;
}
// Time complexity: O(Memo 배열 크기)
// Space complexity: O(Memo 배열 크기)
