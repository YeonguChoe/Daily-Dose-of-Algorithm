// 기본 버전
// Time complexity: O(제곱수^n)
// Space complexity: O(n)

int ways_to_make_remaining(int remaining, vector<int>& square_numbers) {
    if (remaining == 0) {
        return 0;
    }
    if (remaining < 0) {
        return INT_MAX - 1; // 무한대 값을 집어 넣어서 해당 path 제외
    }

    // 피연산자의 개수
    int operand_count = INT_MAX;
    // 제곱수를 하나씩 빼고, 뺐을때 음수이면 해당 path 제외
    for (int x : square_numbers) {
        int result = ways_to_make_remaining(remaining - x, square_numbers);
        // 최소 피연산자의 개수를 찾음
        operand_count = min(min_squares, result + 1);
    }

    return operand_count;
}

int numSquares(int n) {

    // 제곱수 리스트 만들기
    vector<int> square_number_list;
    int i = 1;
    while (i * i <= n) {
        square_number_list.push_back(i * i);
        i += 1;
    }

    int result = ways_to_make_remaining(n, square_number_list);
    return result;
}

// DP 버전
// Time complexity: O(n)
// Space complexity: O(n)

int ways_to_make_remaining(int remaining, vector<int>& square_numbers,
                           int* memoization) {
    if (remaining >= 0 and memoization[remaining] != -1) {
        return memoization[remaining];
    } else if (remaining == 0) {
        return 0;
    } else if (remaining < 0) {
        return INT_MAX - 1; // 무한대 값을 집어 넣어서 해당 path 제외
    }

    // 피연산자의 개수
    int operand_count = INT_MAX;
    // 제곱수를 하나씩 빼고, 뺐을때 음수이면 해당 path 제외
    for (int x : square_numbers) {
        int result = ways_to_make_remaining(remaining - x, square_numbers,
                                            memoization);
        // 최소 피연산자의 개수를 찾음
        operand_count = min(operand_count, result + 1);
    }
    // memoization 테이블에 업데이트함
    memoization[remaining] = operand_count;

    return memoization[remaining];
}

int numSquares(int n) {

    // 제곱수 리스트 만들기
    vector<int> square_number_list;
    int i = 1;
    while (i * i <= n) {
        square_number_list.push_back(i * i);
        i += 1;
    }

    // 메모아이제이션 (기억 테이블;캐시)
    int* memo = new int[n + 1];
    memset(memo, -1, (n + 1) * sizeof(int));

    int result = ways_to_make_remaining(n, square_number_list, memo);
    return result;
}
