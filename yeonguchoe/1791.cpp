// Time complexity: O(edge)
// Space complexity: O(edge)
int findCenter(vector<vector<int>> &edges)
{
    set<int> vertex;
    for (vector<int> e : edges) // O(edges)
    {
        vertex.insert(e[0]);
        vertex.insert(e[1]);
    }

    vector<vector<int>> adjacency_list(vertex.size());

    for (vector<int> e : edges) // O(edges)
    {
        int start = e[0];
        int end = e[1];
        adjacency_list[start - 1].push_back(end);
        adjacency_list[end - 1].push_back(start - 1);
    }

    for (int i = 0; i < adjacency_list.size(); i++) // O(node 종류)
    {
        if (adjacency_list[i].size() == vertex.size() - 1)
        {
            return i + 1;
        }
    }
    return 0;
}
