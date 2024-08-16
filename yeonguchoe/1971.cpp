// Time complexity: O(n+e)
// Space complexity: O(n+e)

bool dfs(vector<vector<int>> &adj, set<int> &visited, int current_node,
         int &destination, int &n)
{
    // 방문한 노드는 이미 방문 했다고 표시
    visited.insert(current_node);

    // 만약에 현재 노드가 목적지 노드인 경우 true 반환
    if (current_node == destination)
    {
        return true;
    }
    for (int child_node : adj[current_node])
    {
        // child 노드가 이미 방문하지 않은 노드인지 검사
        if (visited.find(child_node) == visited.end())
        {
            // 만약에 dfs의 반환값이 true, 즉, 목적지를 찾은 경우 true 반환
            if (dfs(adj, visited, child_node, destination, n) == true)
            {
                return true;
            }
        }
    }
    return false;
}

bool validPath(int n, vector<vector<int>> &edges, int source,
               int destination)
{
    vector<vector<int>> adjacency_list(n);
    set<int> visited; // 방문한 노드는 방문했다고 표시

    // 그래프의 간선들을 인접 리스트로 표현하기
    for (const vector<int> edge : edges)
    {
        int start = edge[0];
        int end = edge[1];
        adjacency_list[start].push_back(end);
        adjacency_list[end].push_back(start);
    }
    bool result = dfs(adjacency_list, visited, source, destination, n);
    return result;
}
