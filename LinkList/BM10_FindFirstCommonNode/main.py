class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        len1 = len2 = 0
        p = pHead1
        q = pHead2
        while p:
            len1 += 1
            p = p.next
        while q:
            len2 += 1
            q = q.next
        p = pHead1
        q = pHead2
        if len1 < len2:
            for i in range(len2-len1):
                q = q.next
        elif len1 > len2:
            for i in range(len1-len2):
                p = p.next
        while p and q:
            if p == q:
                return p
            p = p.next
            q = q.next
        return None
