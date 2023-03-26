class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param root TreeNode类
# @return int整型二维数组
#
class Solution:
    def levelOrder(self , root: TreeNode) -> List[List[int]]: # 思想：队列
        level = []
        res = []
        if root == None:
            return res
        level.append(root)
        while len(level)>0:
            arr = [] # 该层节点
            ans = [] # 该层的值
            while len(level)>0:
                temp = level.pop(0)
                ans.append(temp.val)
                arr.append(temp)
            res.append(ans)
            for i in range(len(arr)):
                if arr[i].left:
                    level.append(arr[i].left)
                if arr[i].right:
                    level.append(arr[i].right)
        return res
