# @param input int整型一维数组
# @param k int整型
# @return int整型一维数组
#
from heapq import *
class Solution:
    def GetLeastNumbers_Solution(self , input: List[int], k: int) -> List[int]:
        heapify(input)
        count = k
        res = []
        while count > 0:
            res.append(heappop(input))
            count -= 1
        return res
