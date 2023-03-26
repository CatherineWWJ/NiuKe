class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param root TreeNode类
# @return int整型二维数组
#
class Solution:
    def levelOrder(self , root: TreeNode) -> List[List[int]]:
        level = []
        res = []
        if root == None:
            return res
        level.append(root)
        while len(level)>0:
            ans = []
            n = len(level)
            for i in range(n): # 每层节点的数量 = 队列大小
                ans.append(level[0].val)
                temp = level.pop(0)
                if temp.left:
                    level.append(temp.left)
                if temp.right:
                    level.append(temp.right)
            res.append(ans)
        return res