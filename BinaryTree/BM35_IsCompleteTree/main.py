class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return bool布尔型
#
from queue import Queue
class Solution:
    def isComplete(self, root: TreeNode) -> bool:
        q = Queue()
        q.put(root)
        flag = False
        while not q.empty() and not flag:
            n = q.qsize()
            for i in range(n):
                temp = q.get()
                if temp == None: # 如果遇到某个节点为空，进行标记，代表到了完全二叉树的最下层
                    flag = True
                    break
                q.put(temp.left)
                q.put(temp.right)
        while not q.empty(): # 后续不应该还存在有效节点！！！
            if q.get():
                return False
        return True

    def isCompleteTree(self , root: TreeNode) -> bool:
        return self.isComplete(root)
