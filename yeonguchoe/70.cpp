// 기본 버전
// Time complexity: O(2^n) 왜냐하면, Leaf까지 가는 경로가 2^n개 있기 떄문에.
// Space complexity: O(n) 왜냐하면, 콜스택의 최대 깊이, 즉 decision트리의 height이 최대 n이기 때문.
int ways_to_make_remaining(int remaining, int goal) {
    if (remaining == 0) {
        return 1;
    } else if (remaining < 0) {
        return 0;
    }
    return ways_to_make_remaining(remaining - 1, goal) +
           ways_to_make_remaining(remaining - 2, goal);
}

int climbStairs(int n) {
    return ways_to_make_remaining(n, n);
}


// Dynamic Programming 버전
// Time complexity: O(n) 왜냐하면, decision 트리를 돌때, 0,1,2,3까지 memoization에 저장 했으면, 그때 부터는 바로 호출 할수 있음.
// Space complexity: O(n) 왜냐하면, 콜스택 깊이가 최대 height이기도 하고, memoization 배열의 크기가 n+1이기 때문.
int ways_to_make_remaining(int remaining, int goal, int* memoization) {
    if (remaining >= 0 and memoization[remaining] > 0) {
        return memoization[remaining];
    } else if (remaining == 0) {
        return 1;
    } else if (remaining < 0) {
        return 0;
    }
    memoization[remaining] =
        ways_to_make_remaining(remaining - 1, goal, memoization) +
        ways_to_make_remaining(remaining - 2, goal, memoization);
    return memoization[remaining];
}

int climbStairs(int n) {
    int* memo = new int[n + 1];
    memset(memo, 0, (n + 1) * sizeof(int));
    return ways_to_make_remaining(n, n, memo);
}
