class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        my = ListNode(-1)
        my.next = None
        p = pHead1
        q = pHead2
        tail = my
        if not (p and q): # 关注：2个链表均为空直接返回！！！
            return pHead1
        while p and q:
            if p.val<=q.val:
                tail.next = p
                tail = p
                p = p.next
            else:
                tail.next = q
                tail = q
                q = q.next
        if p:
            tail.next = p
        if q:
            tail.next = q
        return my.next