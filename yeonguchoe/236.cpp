// Time complexity: O(n)
// Space complexity: O(1)

bool dfs(TreeNode* root, TreeNode* p, TreeNode* q, TreeNode*& LCA) {
    if (root == nullptr) {
        return false;
    }
    bool mid = (root == p or root == q);
    bool left = dfs(root->left, p, q, LCA);
    bool right = dfs(root->right, p, q, LCA);
    if (mid + left + right >= 2) {
        LCA = root;
    }
    return mid or left or right;
}

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    TreeNode* result = nullptr;
    dfs(root, p, q, result);
    return result;
}
