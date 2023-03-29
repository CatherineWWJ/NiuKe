# -*- coding:utf-8 -*-
from heapq import *
class Solution:
    def __init__(self):
        self.min = []  # 大顶堆：堆顶为较小的数
        self.max = []  # 小顶堆：堆顶为较大的数

    def Insert(self, num):
        heappush(self.min, -num)
        heappush(self.max, -heappop(self.min))
        while len(self.min) < len(self.max):
            heappush(self.min, -heappop(self.max))

    def GetMedian(self):
        if len(self.min) > len(self.max):
            return -self.min[0]
        else:
            return (-self.min[0] + self.max[0]) / 2
