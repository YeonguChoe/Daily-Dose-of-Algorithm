// Time complexity: O(n^2)
// Space complexity: O(n)

long long maximumImportance(int n, vector<vector<int>>& roads)
{
    vector<long long> edges_from_node(n, 0);

    for (vector<int>& road : roads)
    {
        edges_from_node[road[0]] += 1;
        edges_from_node[road[1]] += 1;
    }

    // 간선을 오름차순으로 정렬
    sort(edges_from_node.begin(), edges_from_node.end());

    long long total_importance = 0;

    // 중요도의 합 계산
    for (int node = 0; node < n; node++)
    {
        // v(노드)가 1부터 시작 하기 때문에 (node + 1)이됨
        total_importance += (edges_from_node[node] * (node + 1));
    }
    return total_importance;
}
