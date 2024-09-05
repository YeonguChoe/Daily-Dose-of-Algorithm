// Time complexity: O(n)
// Space complexity: O(1)

ListNode * removeNthFromEnd(ListNode * head, int n) {

  // 1단계: 총 Node 개수를 구함
  int total_node_count = 1;
  ListNode * pointer = head;

  while (pointer -> next != nullptr) {
    total_node_count += 1;
    pointer = pointer -> next;
  }

  // 2단계: 노드 제거

  // edge 케이스1: 노드의 개수가 1개인 경우, 해당 노드 제거
  if (total_node_count == 1) {
    head = nullptr;
    return nullptr;
  }

  // 제거하려는 노드가 몇번째 노드인지 구함.
  int node_of_n = total_node_count - n;

  // edge 케이스2: 첫번째 시작 노드를 지워야 하는 경우, 첫번째 노드를 지우고, 두번째 노드 반환
  if (node_of_n == 0) {
    ListNode * temp = head;
    head = head -> next;
    temp -> next = nullptr;
    return head;
  }

  // 위의 2가지 edge 케이스가 아닌 경우,
  // 맨뒤 노드에서 n-1번째 노드 제거
  pointer = head; // 노드를 다시 맨 앞으로 이동

  // 포인터를 제거하려는 노드 이전 노드 까지 이동시킴.
  for (int i = 0; i < node_of_n - 1; i++) {
    pointer = pointer -> next;
  }

  // 노드 제거 작업
  ListNode * temp = pointer -> next;
  pointer -> next = pointer -> next -> next;
  temp -> next = nullptr;

  // 연결 리스트의 시작 노드 반환
  return head;
}
