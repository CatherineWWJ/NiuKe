class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param pRoot TreeNode类 
# @return bool布尔型
#
class Solution:
    def isBalance(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.isBalance(root.left)
        right = self.isBalance(root.right)
        if left == -1 or right == -1 or abs(left-right)>1: # 出现非平衡二叉树（特殊值标记法）
            return -1
        else:
            return max(left, right)+1

    def IsBalanced_Solution(self , pRoot: TreeNode) -> bool:
        if pRoot == None:
            return True
        # if self.isBalance(pRoot) == -1:
        #     return False
        # return True
        # 参考答案之后的优化写法：
        return self.isBalance(pRoot) != -1
