
## Reverse Linked List
링크: [https://leetcode.com/problems/reverse-linked-list/description/](https://leetcode.com/problems/reverse-linked-list/description/)

<br/>

### Swift

#### 풀이
- 비어있는 노드를 생성한다.
- head.next 를 미리 다른 곳에 넣어둔다.
- 이제 노드를 거꾸로 돌리기위해 head.next에 만들어둔 빈노드를 할당하고,
- 빈노드에는 현재 head를 놓는다.
- 이제 한번 뒤집었으니 다음껄 뒤집으로 미리 넣어둔 head.next를 head에 할당한다.

```swift
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

class Solution {
    func reverseList(_ head: ListNode?) -> ListNode? {
        var node: ListNode? = nil
        var head = head
        
        while head != nil {
            let node2 = head?.next
            head?.next = node
            node = head
            head = node2
        }
        return node
    }
}
```

<br/>

#

### Dart 

```dart
class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

class Solution {
  ListNode? reverseList(ListNode? head) {
    ListNode? node1 = null;

    while (head != null) {
      final node2 = head.next;
      head.next = node1;
      node1 = head;
      head = node2;
    }

    return node1;
  }
}
```
