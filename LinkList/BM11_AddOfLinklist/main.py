class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
#
class Solution:
    def addInList(self, head1: ListNode, head2: ListNode) -> ListNode:
        my1 = ListNode(-1)
        my2 = ListNode(-1)
        my1.next = head1
        my2.next = head2
        cur = head1
        while cur.next:
            temp = cur.next
            cur.next = temp.next
            temp.next = my1.next
            my1.next = temp
        cur = head2
        while cur.next:
            temp = cur.next
            cur.next = temp.next
            temp.next = my2.next
            my2.next = temp
        c = 0
        p = my1
        q = my2
        ans = ListNode(-1)
        ans.next = None
        while p.next and q.next:
            temp = p.next.val + q.next.val + c
            one = ListNode(temp % 10)
            one.next = ans.next
            ans.next = one
            c = temp // 10
            p = p.next
            q = q.next
        while p.next:
            temp = p.next.val + c
            one = ListNode(temp % 10)
            one.next = ans.next
            ans.next = one
            c = temp // 10
            p = p.next
        while q.next:
            temp = q.next.val + c
            one = ListNode(temp % 10)
            one.next = ans.next
            ans.next = one
            c = temp // 10
            q = q.next
        if c != 0:
            one = ListNode(c)
            one.next = ans.next
            ans.next = one
        return ans.next


