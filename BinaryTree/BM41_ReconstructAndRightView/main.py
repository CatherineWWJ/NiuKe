#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 求二叉树的右视图
# @param xianxu int整型一维数组 先序遍历
# @param zhongxu int整型一维数组 中序遍历
# @return int整型一维数组
#
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def restruct(self, pre: List[int], mid: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        c = mid.index(pre[0])
        left = self.restruct(pre[1:1 + c], mid[0:c])
        right = self.restruct(pre[1 + c:], mid[c + 1:])
        root.left = left
        root.right = right
        return root

    def solve(self, xianxu: List[int], zhongxu: List[int]) -> List[int]:
        root = self.restruct(xianxu, zhongxu)
        q = []
        res = []
        if not root:
            return res
        q.append(root)
        while len(q) > 0:
            n = len(q)
            res.append(q[n - 1].val)
            for i in range(n):
                temp = q.pop(0)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return res