class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        my = ListNode(-1)
        my.next = pHead
        p = q = my
        for i in range(0,k):
            p = p.next # p,q起始位置在链表头结点，先动指针后判断；起始在首元节点，先判断后动指针
            if not p:
                return p
        while p:
            p = p.next
            q = q.next
        return q