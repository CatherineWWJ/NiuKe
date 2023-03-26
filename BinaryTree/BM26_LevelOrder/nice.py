class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param root TreeNode类
# @return int整型二维数组
#
from queue import Queue
class Solution:
    def levelOrder(self , root: TreeNode) -> List[List[int]]:
        res = []
        if root == None:
            return res
        q = Queue() # 队列
        q.put(root) # 入队
        while not q.empty(): # 队列判空
            row = []
            n = q.qsize() # 获取队列大小
            for i in range(n):
                cur = q.get() # 出队
                row.append(cur.val)
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
            res.append(row)
        return res