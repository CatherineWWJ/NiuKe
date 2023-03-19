class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode: # 直接比较删除重复节点
        if head == None:
            return None
        res = ListNode(-1)
        res.next = head
        cur = res
        while cur.next and cur.next.next: # 至少存在2个节点！！！
            if cur.next.val == cur.next.next.val: # 判断节点同值
                temp = cur.next.val
                while cur.next and cur.next.val == temp:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return res.next