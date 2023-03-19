class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode:
        if not head:
            return head
        p = head
        while p.next:
            if p.next.val == p.val:
                temp = p.next.next
                p.next = temp
            else:
                p = p.next
        return head