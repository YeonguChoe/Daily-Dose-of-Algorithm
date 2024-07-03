// Unfinished

bool dfs_pacific(int i, int j, vector<vector<int>>& map, vector<vector<bool>>& visited)
{
    int row = map.size();
    int column = map[0].size();

    // 벽에 붙는지 체크
    if (i <= 0 || j <= 0)
    {
        return true;
    }

    // Mark the current cell as visited
    visited[i][j] = true;

    if (i < row - 2 && map[i + 1][j] <= map[i][j] && !visited[i + 1][j])
    {
        return dfs_pacific(i + 1, j, map, visited);
    }
    if (j < column - 2 && map[i][j + 1] <= map[i][j] && !visited[i][j + 1])
    {
        return dfs_pacific(i, j + 1, map, visited);
    }
    if (i > 0 && map[i - 1][j] <= map[i][j] && !visited[i - 1][j])
    {
        return dfs_pacific(i - 1, j, map, visited);
    }
    if (j > 0 && map[i][j - 1] <= map[i][j] && visited[i][j - 1])
    {
        return dfs_pacific(i, j - 1, map, visited);
    }
    visited[i][j] = false;
    return false;
}

bool dfs_atlantic(int i, int j, vector<vector<int>>& map, vector<vector<bool>>& visited)
{
    int row = map.size();
    int column = map[0].size();

    // 벽에 붙는지 체크
    if (i >= row - 1 || j >= column - 1)
    {
        return true;
    }

    // Mark the current cell as visited
    visited[i][j] = true;

    if (i < row - 2 && map[i + 1][j] <= map[i][j] && !visited[i + 1][j])
    {
        return dfs_atlantic(i + 1, j, map, visited);
    }
    if (j < column - 2 && map[i][j + 1] <= map[i][j] && !visited[i][j + 1])
    {
        return dfs_atlantic(i, j + 1, map, visited);
    }
    if (i > 0 && map[i - 1][j] <= map[i][j] && !visited[i - 1][j])
    {
        return dfs_atlantic(i - 1, j, map, visited);
    }
    if (j > 0 && map[i][j - 1] <= map[i][j] && visited[i][j - 1])
    {
        return dfs_atlantic(i, j - 1, map, visited);
    }
    visited[i][j] = false;
    return false;
}


vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights)
{
    vector<vector<int>> result;

    vector<vector<bool>> visited_cell1(heights.size(), vector<bool>(heights[0].size(), false));
    vector<vector<bool>> visited_cell2(heights.size(), vector<bool>(heights[0].size(), false));

    for (int i = 1; i < heights.size() - 1; i++)
    {
        for (int j = 1; j < heights[0].size() - 1; j++)
        {
            if (dfs_pacific(i, j, heights, visited_cell1) &&
                dfs_atlantic(i, j, heights, visited_cell2))
            {
                result.push_back({i, j});
            }
        }
    }
    return result;
}
