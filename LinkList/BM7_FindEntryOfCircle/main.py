# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead == None or pHead.next == None:
            return None
        fast = slow = pHead
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == None: # 无法形成闭环
                return None
            if fast == slow: # 快慢指针在环中某处相遇
                break
        fast = pHead
        while fast != slow: # 解题关键：数学公式推算
            fast = fast.next
            slow = slow.next
        return slow
