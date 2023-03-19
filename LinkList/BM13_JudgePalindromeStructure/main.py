class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def isPail(self , head: ListNode) -> bool:
        if not head or not head.next:
            return True
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        print(fast.val, slow.val)
        while fast.next: # 这里fast始终未变，待插节点始终为fast.next，此处循环判断条件为（是否还存在待插节点）
            temp = fast.next
            fast.next = temp.next
            temp.next = slow.next
            slow.next = temp
        fast = head
        slow = slow.next
        while fast and slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True

