// Time complexity: O(n)
// Space complexity: O(n)

bool hasPathSum(TreeNode* root, int targetSum)
{
    if (!root)
    {
        return false;
    }
    targetSum -= root->val;
    if (!root->left and !root->right)
    {
        return targetSum == 0;
    }
    return hasPathSum(root->left, targetSum) or
        hasPathSum(root->right, targetSum);
}
