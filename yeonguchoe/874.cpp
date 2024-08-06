// Time complexity: O(n^2)
// Space complexity: O(n)
int robotSim(vector<int>& commands, vector<vector<int>>& obstacles)
{
    array<int, 2> current_location = {0, 0};
    array<int, 2> current_direction = {0, 1};
    int furthest_euclidean_distance = 0;

    // obstacle들을 key를 x좌표, value를 y좌표들로 정리해 놓았습니다.
    unordered_map<int, set<int>> obstacle_x_to_y;

    for (vector<int> i : obstacles)
    {
        obstacle_x_to_y[i[0]].insert(i[1]);
    }

    for (int i = 0; i < commands.size(); i++)
    {
        int selected_command = commands[i];

        // 왼쪽으로 90도 이동하는 경우 방향을 다음과 같이 계산합니다.
        if (selected_command == -2)
        {
            current_direction = {
                -current_direction[1],
                current_direction[0]
            };
        }
        // 오른쪽으로 90도 회전하는 경우 방향을 다음과 같이 계산합니다.
        if (selected_command == -1)
        {
            current_direction = {
                current_direction[1],
                -current_direction[0]
            };
        }

        // while문은 command의 개수만큼 앞으로 이동하는 것을 한칸을 이동할때마다 1번의 loop로 합니다.
        while (selected_command > 0)
        {
            // 만약에 앞으로 이동 했을때, obstacle과 겹치는 경우 while문을 break해서 나옵니다.
            vector<int> future_location = {
                current_location[0] + current_direction[0],
                current_location[1] + current_direction[1]
            };
            if (obstacle_x_to_y[future_location[0]].find(
                    future_location[1]) !=
                obstacle_x_to_y[future_location[0]].end())
            {
                break;
            }
            // obstacle이 없는 경우, 설정된 이동 방향만큼 한번 이동합니다.
            current_location[0] += current_direction[0];
            current_location[1] += current_direction[1];
            selected_command--;
        }
        // [0,0] 시작점으로 부터 최대로 떨어졌을때의 최단거리를 구합니다.
        int current_euclidean_distance =
            pow(current_location[0], 2) + pow(current_location[1], 2);
        furthest_euclidean_distance =
            max(furthest_euclidean_distance, current_euclidean_distance);
    }
    return furthest_euclidean_distance;
}
