# @param num int整型一维数组
# @param size int整型
# @return int整型一维数组
#
class Solution: # 思路：双端队列
    def maxInWindows(self, num: List[int], size: int) -> List[int]:
        res = []
        if size <= len(num) and size != 0: # 存在解
            from collections import deque
            dq = deque()
            for i in range(size): # 先遍历一个窗口
                while len(dq) > 0 and num[dq[-1]] < num[i]: # 去掉比自己先进队列的小于自己的值
                    dq.pop()
                dq.append(i)
            # 每获得一个新窗口，就出现一个窗口最大值
            for i in range(size, len(num)): # 遍历后续数组元素
                res.append(num[dq[0]]) # 队头一定是当前窗口的最大值！！！如果后面有比它大的，它早已被去掉了~
                while len(dq) > 0 and dq[0] < i - size + 1: # 弹出窗口移动后不在窗口的值
                    dq.popleft()
                while len(dq) > 0 and num[dq[-1]] < num[i]: # 加入新的值前，去掉比自己先进队列的小于自己的值
                    dq.pop()
                dq.append(i)
            res.append(num[dq[0]]) # 最后一个值加入后，保存窗口最大值
        return res # 不存在解就直接返回
