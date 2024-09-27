// Time complexity: O(n)
// Space complexity: O(n)
class Solution {
public:
    void paste(TreeNode* node, int level, vector<vector<int>>& target) {
        if (node == nullptr) {
            return;
        }
        // level이 존재하지 않는경우
        if (target.size() == level) {
            vector<int> i;
            // 새로운 level 생성
            target.push_back(i);
        }
        target[level].push_back(node->val);
        // 왼쪽 child가 존재시, paste 함수 호출
        if (node->left != nullptr) {
            paste(node->left, level + 1, target);
        }
        // 오른쪽 child가 존재시, paste 함수 호출
        if (node->right != nullptr) {
            paste(node->right, level + 1, target);
        }
    }

    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        paste(root, 0, result);
        return result;
    }
};
