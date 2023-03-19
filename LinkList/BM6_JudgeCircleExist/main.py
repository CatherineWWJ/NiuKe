class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head ListNode类
# @return bool布尔型
#
class Solution:
    def hasCycle(self , head: ListNode) -> bool:
        if head is None:
            return False
        my = ListNode(-1)
        my.next = head
        p = q = my
        while p and q:
            if p == q and p != my:
                return True
            if not p.next:
                return False
            p = p.next.next
            q = q.next
        return False