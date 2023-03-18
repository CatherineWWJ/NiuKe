class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
        #加个表头
        res = ListNode(-1)
        res.next = head
        #前序节点
        pre = res
        #当前节点
        cur = head
        #找到m
        for i in range(1,m): # ！！！
            pre = cur
            cur = cur.next
        #从m反转到n
        for i in range(m, n):
            temp = cur.next
            cur.next = temp.next # ！！！无需标记区间头
            temp.next = pre.next
            pre.next = temp
        #返回去掉表头
        return res.next
