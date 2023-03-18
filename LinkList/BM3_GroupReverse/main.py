class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def reverseKGroup(self , head: ListNode, k: int) -> ListNode:
        # write code here
        my = ListNode(-1)
        my.next = head
        pre = my
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        print(count)
        cur = head
        for i in range(1,count-count%k+1): # 关键点：控制循环
            if i%k == 0: # 关键点：前插法的pre指针位置
                pre = cur
                cur = cur.next
            else:
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
        return my.next