// Time complexity: O(n)
// Space complexity: O(n)

bool hasCycle(ListNode* head)
{
    set<ListNode*> visited;
    ListNode* observing_node = head;

    while (observing_node != nullptr)
    {
        if (visited.find(observing_node) != visited.end())
        {
            return true;
        }
        visited.insert(observing_node);
        observing_node = observing_node->next;
    }
    return false;
}
