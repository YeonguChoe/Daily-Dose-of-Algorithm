// Time complexity: O(6^n)
// Space complexity: O(n)

bool backtracking(int current_sum, int goal, int remaining_n,
                  vector<int>& combination, vector<int>& answer) {
    // 나머지 횟수가 0이고 합이 goal에 도달한 경우.
    if (remaining_n == 0 and current_sum == goal) {
        answer = combination;
        return true;
    }
    // 나머지 횟수만 다 소진한 경우.
    if (remaining_n == 0) {
        return false;
    }

    // 나머지 횟수가 남았지만, 이미 합이 초과한 경우
    if (current_sum > goal) {
        return false;
    }

    // 값을 붙였다가 뗏다가 하면서 백트래킹
    for (int i = 6; i > 0; --i) {
        combination.push_back(i);
        if (backtracking(current_sum + i, goal, remaining_n - 1,
                         combination, answer)) {
            return true;
        }
        combination.pop_back();
    }

    return false;
}

vector<int> missingRolls(vector<int>& rolls, int mean, int n) {

    // 1 단계: 나머지 계산하기
    int remaining_sum = mean * (n + rolls.size());

    for (int r : rolls) {
        remaining_sum -= r;
    }

    // 불가능한 경우 확인
    if (remaining_sum < n or remaining_sum > 6 * n) {
        return {};
    }

    // 2단계: 백트래킹
    vector<int> empty_combination;
    vector<int> result;
    backtracking(0, remaining_sum, n, empty_combination, result);
    return result;
}
