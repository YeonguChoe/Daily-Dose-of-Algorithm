// Time complexity: O(n)
// Space complexity: O(n)
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {

    // 트리의 구조 비교
    if (p == NULL && q == NULL) {
        return true;
    }
    if (p == NULL && q != NULL) {
        return false;
    }
    if (p != NULL && q == NULL) {
        return false;
    }

    // 노드의 구조 비교
    if (p->val != q->val) {
        return false;
    }
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}
