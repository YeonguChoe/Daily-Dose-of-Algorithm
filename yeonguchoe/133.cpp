// Time complexity: O(Vertex+Edge)
// Space complexity: O(Vertex)
unordered_map<Node*, Node*> visited;

Node* cloneGraph(Node* node)
{
    // 베이스 케이스
    if (node == NULL)
    {
        return node;
    }
    // visited 맵에 이미 그래프의 일부분인 특정 root으로부터 시작하는
    // 구조체가 있는경우
    if (visited.find(node) != visited.end())
    {
        return visited[node];
    }
    // 구조체를 복사한후 구조체의 root 반환
    Node* cloneNode = new Node(node->val, {});
    visited[node] = cloneNode;
    for (Node* neighbor : node->neighbors)
    {
        cloneNode->neighbors.push_back(cloneGraph(neighbor));
    }
    return cloneNode;
}
