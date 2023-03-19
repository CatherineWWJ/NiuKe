class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head ListNode类 the head node
# @return ListNode类
#
class Solution: # 分治：归并
    def merge(self, pHead1: ListNode, pHead2: ListNode): # 合并2个有序链表
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        head = ListNode(-1)
        cur = head
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        if pHead1:
            cur.next = pHead1
        if pHead2:
            cur.next = pHead2
        return head.next

    def sortInList(self, head: ListNode) -> ListNode: # 从中间将链表划分为二
        if head == None or head.next == None:
            return head
        left = head
        mid = head.next
        right = head.next.next
        while right and right.next:
            mid = mid.next
            left = left.next
            right = right.next.next
        left.next = None # ！！！断开
        return self.merge(self.sortInList(head), self.sortInList(mid))