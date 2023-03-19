class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None or head.next.next == None:
            return head
        pre = head          # pre 标记奇数链表表尾
        tail = head.next    # tail标记偶数链表表尾
        while tail and tail.next: # 待插节点为tail.next
            temp = tail.next
            tail.next = temp.next
            temp.next = pre.next
            pre.next = temp
            # 每次插入一个正确的奇数位置节点，同时获得一个正确的偶数位置节点
            pre = pre.next
            tail = tail.next
        return head

