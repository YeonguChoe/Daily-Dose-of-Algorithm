// Using 3 pointers
// Time Complexity: O(n)
// Space Complexity: O(1): ptr1, ptr2, ptr3
ListNode* reverseList(ListNode* head)
{
    if (head == nullptr)
    {
        return head;
    }
    if (head->next == nullptr)
    {
        return head;
    }

    ListNode* ptr1 = head;
    ListNode* ptr2 = (head->next);
    ListNode* ptr3 = (ptr2->next);
    ptr1->next = nullptr;
    while (ptr3 != nullptr)
    {
        ptr2->next = ptr1;
        ptr1 = ptr2;
        ptr2 = ptr3;
        ptr3 = ptr3->next;
    }
    ptr2->next = ptr1;
    return ptr2;
}
