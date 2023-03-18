class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        my = ListNode(None)
        my.next = head
        count = 1
        p = my.next
        front = rear = my
        while p:
            if count < m:
                p = p.next
                front = front.next
                rear = rear.next
                count += 1
            if m <= count <= n:
                if count == m:
                    front.next = None
                    rear = p
                q = p
                p = p.next
                count += 1
                q.next = front.next
                front.next = q
                continue
            if count > n:
                rear.next = p
                break
        return my.next
