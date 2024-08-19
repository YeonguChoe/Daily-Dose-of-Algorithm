// Time complexity: O(edge수+node수)
// Space complexity: O(node수)

// true: cycle 발견함
// false: cycle 발견 못함
bool dfs_cycle_detector(int root, vector<vector<int>> &adjacency_list,
                        vector<bool> &on_cycle, vector<bool> &checked)
{
    // 현재 노드가 path위에 있는 노드 였던 경우.
    if (on_cycle[root])
    {
        return true;
    }
    // 현재 노드가 path위에 없고, 이미 검사한 노드인 경우.
    else if (checked[root])
    {
        return false;
    }

    // 현재 노드를 path위 있다고 추가
    on_cycle[root] = true;
    // 현재 노드를 검사했다고 마킹
    checked[root] = true;

    // 현재 노드에 연결된 노드들 검사
    for (int connected : adjacency_list[root])
    {
        // 싸이클이 존재하면, 해당 path에 있는 모든 노드를 true 상태로
        // 유지하고 더이상 진행하지 않음.
        if (dfs_cycle_detector(connected, adjacency_list, on_cycle,
                               checked))
        {
            // 싸이클 발견
            return true;
        }
    }
    // 싸이클이 발견되지 않은 경우. 즉 현재 노드에서 출발한 모든 연결된
    // 노드들이 Leaf까지 도달한 경우
    on_cycle[root] = false;
    return false;
}

vector<int> eventualSafeNodes(vector<vector<int>> &graph)
{
    // 노드의 개수
    int node_count = graph.size();
    // 싸이클위에 있는 노드 기록 (true: 싸이클 위의 노드, false: 싸이클 위에 없는 노드)
    vector<bool> on_cycle(node_count);
    // 이미 검사한 노드 기록 (true: 이미 검사, false: 아직 검사 안함)
    vector<bool> checked_node(node_count);

    // 각 노드를 시작점으로 cycle detector를 실행
    for (int i = 0; i < node_count; i++)
    {
        dfs_cycle_detector(i, graph, on_cycle, checked_node);
    }

    // 결과값: 싸이클위에 없는 노드들의 모음
    vector<int> result;
    for (int n = 0; n < node_count; n++)
    {
        // 싸이클 위에 없는 노드만, 결과값에 추가
        if (on_cycle[n] == false)
        {
            result.push_back(n);
        }
    }
    return result;
}
