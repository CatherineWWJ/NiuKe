class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head ListNode类
# @param n int整型
# @return ListNode类
#
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        my = ListNode(-1)
        my.next = head
        p = q = my
        for i in range(n):
            p = p.next
        while p.next:
            p = p.next
            q = q.next
        temp = q.next
        q.next = temp.next
        return my.next
