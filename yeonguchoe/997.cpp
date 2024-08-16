// Time complexity: O(trust)
// Space complexity: O(n)
int findJudge(int n, vector<vector<int>> &trust)
{
    // element: index 노드로 들어오는 화살표 개수
    vector<int> in_degree(n, 0);
    // element: index 노드에서 나가는 화살표 개수
    vector<int> out_degree(n, 0);

    for (vector<int> t : trust)
    {
        // 노드에서 나가는 화살표 갱신
        out_degree[t[0] - 1] += 1;
        // 노드로 들어오는 화살표 갱신
        in_degree[t[1] - 1] += 1;
    }

    for (int i = 0; i < n; i++)
    {
        // 2가지 조건을 만족하는 노드가 있는지 확인
        if (in_degree[i] == n - 1 and out_degree[i] == 0)
        {
            return i + 1;
        }
    }
    return -1;
}
