class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue

class Solution:
    def isCompleteTree(self , root: TreeNode) -> bool:
        # 空树一定是完全二叉树
        if not root:
            return True
        q = queue.Queue()
        # 根节点先访问
        q.put(root)
        # 定义一个首次出现的标记位
        flag = False
        # 层次遍历
        while not q.empty():
            sz = q.qsize()
            for i in range(sz):
                cur = q.get()
                # 标记第一次遇到空节点
                if not cur:
                    flag = True
                else:
                    # 后续访问已经遇到过空节点了（优化点！！！）
                    if flag:
                        return False
                    q.put(cur.left)
                    q.put(cur.right)
        return True
