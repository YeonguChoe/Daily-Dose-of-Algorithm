// n: 노드의 개수
// Time complexity: O(n)
// Space complexity: O(n) set의 크기가 n까지 커질수 있음.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode *detectCycle(ListNode *head)
{

    // 만약에 시작 노드조차 없다면 바로 반환
    if (head == nullptr)
    {
        return nullptr;
    }

    set<ListNode *> already_included;
    already_included.insert(head);
    // null pointer가 없으면 앞으로 이동
    while (head->next != nullptr)
    {
        // 만약에 포함이 안되어 있다면,
        if (already_included.find(head->next) == already_included.end())
        {
            // set에 해당 노드를 집어 넣음
            already_included.insert(head->next);
            head = head->next;
        }
        else
        {
            // 만약에 포함이 되어 있다면, 바로 반환
            return head->next;
        }
    }
    return nullptr;
}
