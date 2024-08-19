// Time complexity: O(n^2)
// Space complexity: O(n)
class UnionFind
{
private:
    vector<int> parent;
    int count;

public:
    // Union find 자료구조 초기화
    UnionFind(int size)
    {
        parent.resize(size);
        count = size;
        for (int i = 0; i < count; i++)
        {
            parent[i] = i;
        }
    }

    // Find 연산 정의
    // 하는일: representative 노드를 찾음
    int find(int x)
    {
        if (parent[x] != x)
        {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // Union 연산 정의
    //  하는일: 2개의 component를 합침
    void union_set(int x, int y)
    {
        int x_representative = find(x);
        int y_representative = find(y);
        parent[x_representative] = y_representative;
    }
};

class Solution
{
public:
    int findCircleNum(vector<vector<int>> &isConnected)
    {
        int node_count = isConnected.size();
        UnionFind provinces(node_count);
        int province_count = node_count;

        for (int i = 0; i < node_count; i++)
        {
            for (int j = i + 1; j < node_count; j++)
            {
                if (isConnected[i][j] and
                    provinces.find(i) != provinces.find(j))
                {
                    province_count -= 1;
                    provinces.union_set(i, j);
                }
            }
        }
        return province_count;
    }
};
