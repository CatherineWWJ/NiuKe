from itertools import count
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        if head is None:
            return head
        tail = head
        current = head.next
        while current:
            p = current.next
            current.next = tail
            tail = current
            current = p
        head.next = None
        return tail

