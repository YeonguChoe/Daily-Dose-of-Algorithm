// Time complexity: O(n)
// Space complexity: O(n)

int diameterOfBinaryTree(TreeNode* root)
{
    int result = 0;
    helper(root, result);
    return result;
}

int helper(TreeNode* node, int& diameter)
{
    if (!node)
    {
        return 0;
    }

    int left_height = helper(node->left, diameter);
    int right_height = helper(node->right, diameter);

    diameter = max(diameter, left_height + right_height);

    return 1 + max(left_height, right_height);
}
