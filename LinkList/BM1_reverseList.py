from itertools import count
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
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

