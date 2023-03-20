class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param lists ListNode类一维数组
# @return ListNode类
#

from heapq import *
import itertools

# 产生一个从0开始的序列
counter = itertools.count() # 解决堆出现优先级相同的bug（无法比较元组进行堆排序）


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        my = []
        for i in range(len(lists)):
            if lists[i] != None: # 当链表为空，不需要合并
                heappush(my, (lists[i].val, next(counter), lists[i]))
        ans = ListNode(-1)
        tail = ans
        while len(my) > 0:
            p = heappop(my)[2]
            if p.next:
                heappush(my, (p.next.val, next(counter), p.next))
            p.next = None
            tail.next = p
            tail = p
        return ans.next
