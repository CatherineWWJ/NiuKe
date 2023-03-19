class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode:
        if  not head or not head.next:
            return head
        my = ListNode(-1)
        my.next = head
        pre = my
        tag = head
        while tag: # 循环判断条件：以tag起始的同值子链表是否该删
            cur = tag.next
            if not cur: # tag后不存在节点
                break
            if cur.val == tag.val: # tag该删
                while cur and cur.val == tag.val:
                    cur = cur.next
                pre.next = cur
                tag = cur
            else: # tag不该删
                pre = tag
                tag = cur
        return my.next