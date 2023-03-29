# -*- coding:utf-8 -*-
from heapq import *
class Solution:
    def __init__(self):
        self.arr = []
    def Insert(self, num):
        heappush(self.arr, num)
    def GetMedian(self):
        n = len(self.arr)
        temp = []
        if n%2 == 0:
            count = n//2-1
        else:
            count = n//2
        for i in range(count):
            temp.append(heappop(self.arr))
        if n%2 == 0:
            data1 = heappop(self.arr)
            data2 = heappop(self.arr)
            temp.append(data1)
            temp.append(data2)
            res = (data1+data2)/2
        else:
            data = heappop(self.arr)
            temp.append(data)
            res = data
        while len(temp)>0:
            heappush(self.arr, temp.pop())
        return res