class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param pRoot TreeNode类
# @return int整型二维数组
#
from collections import deque
class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        res = []
        if pRoot == None:
            return res
        q = deque() # 双端队列
        q.append(pRoot)
        flag = True # 判断从左到右 or 从右到左输出
        while len(q)>0:
            row = []
            n = len(q)
            for i in range(n):
                if flag:
                    temp = q.popleft()
                    row.append(temp.val)
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                else:
                    temp = q.pop()
                    row.append(temp.val)
                    if temp.right: # 注意这里的顺序
                        q.appendleft(temp.right)
                    if temp.left:
                        q.appendleft(temp.left)
            res.append(row)
            flag = not flag
        return res
