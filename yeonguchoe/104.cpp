// Time complexity: O(n)
// Space complexity: O(n)

int maxDepth(TreeNode* root)
{
    if (!root)
    {
        return 0;
    }
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}
