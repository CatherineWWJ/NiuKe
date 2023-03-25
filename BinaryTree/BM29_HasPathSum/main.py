class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param root TreeNode类
# @param sum int整型
# @return bool布尔型
#
class Solution:
    def hasPath(self, root: TreeNode, sum: int) -> bool:
        if root.left == None and root.right == None: # 注意：路径的终点必须是叶子节点
            if sum == root.val:
                return True
            else:
                return False
        l_tag = self.hasPath(root.left, sum - root.val) if root.left else False
        r_tag = self.hasPathSum(root.right, sum - root.val) if root.right else False
        return l_tag or r_tag

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        return self.hasPath(root, sum)
