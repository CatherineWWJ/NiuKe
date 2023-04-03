# @param num int整型一维数组
# @param size int整型
# @return int整型一维数组
#
class Solution:
    def maxInWindows(self, num: List[int], size: int) -> List[int]:
        n = len(num)
        if size > n or size == 0:
            return []
        res = [] # 结果数组
        win = [] # 窗口数组
        for i in range(size):
            win.append(num[i])
        res.append(max(win))
        i = size
        while i < n:
            win.pop(0)
            win.append(num[i])
            res.append(max(win))
            i += 1
        return res
