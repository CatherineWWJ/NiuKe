# @param a int整型一维数组
# @param n int整型
# @param K int整型
# @return int整型
#
class Solution:
    def findKth(self , a: List[int], n: int, K: int) -> int:
        a.sort()
        return a[-K]