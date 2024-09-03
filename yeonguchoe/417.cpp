class Solution {
public:
    std::vector<std::vector<int>> surrounding = {
        {1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    struct Compare {
        bool operator()(vector<int>& a,
                        vector<int>& b) const {
            return a[0] < b[0] || (a[0] == b[0] && a[1] < b[1]);
        }
    };

    std::set<std::vector<int>, Compare>
    BFS(std::queue<std::vector<int>> q,
        const std::vector<std::vector<int>>& matrix) {
        std::set<std::vector<int>, Compare> unique_cell;
        std::vector<std::vector<bool>> visited(
            matrix.size(), std::vector<bool>(matrix[0].size(), false));

        while (!q.empty()) {
            vector<int> cell = q.front();
            q.pop();
            int r = cell[0], c = cell[1];
            if (visited[r][c])
                continue;
            visited[r][c] = true;
            unique_cell.insert(cell);

            for (vector<int>& direction : surrounding) {
                int new_row = r + direction[0];
                int new_column = c + direction[1];

                if (new_row >= 0 && new_column >= 0 &&
                    new_row < matrix.size() && new_column < matrix[0].size()) {
                    if (!visited[new_row][new_column] &&
                        matrix[new_row][new_column] >= matrix[r][c]) {
                        q.push({new_row, new_column});
                    }
                }
            }
        }

        return unique_cell;
    }

    std::vector<std::vector<int>>
    pacificAtlantic(std::vector<std::vector<int>>& heights) {
        std::queue<std::vector<int>> pacific_queue;
        std::queue<std::vector<int>> atlantic_queue;

        for (int i = 0; i < static_cast<int>(heights[0].size()); i++) {
            pacific_queue.push({0, i});
            atlantic_queue.push({static_cast<int>(heights.size()) - 1, i});
        }

        for (int j = 0; j < static_cast<int>(heights.size()); j++) {
            pacific_queue.push({j, 0});
            atlantic_queue.push({j, static_cast<int>(heights[0].size()) - 1});
        }

        std::set<std::vector<int>, Compare> reachable_from_pacific =
            BFS(pacific_queue, heights);
        std::set<std::vector<int>, Compare> reachable_from_atlantic =
            BFS(atlantic_queue, heights);

        std::vector<std::vector<int>> result;
        std::vector<std::vector<int>> intersection;

        intersection.reserve(
            min(static_cast<int>(reachable_from_pacific.size()),
                     static_cast<int>(reachable_from_atlantic.size())));

        set_intersection(
            reachable_from_pacific.begin(), reachable_from_pacific.end(),
            reachable_from_atlantic.begin(), reachable_from_atlantic.end(),
            back_inserter(intersection));

        return intersection;
    }
};
