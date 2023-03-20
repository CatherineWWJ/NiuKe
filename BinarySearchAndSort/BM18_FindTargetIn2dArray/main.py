# @param target int整型
# @param array int整型二维数组
# @return bool布尔型
#
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        if len(array) == 0:
            return False
        if len(array[0]) == 0:
            return False
        n = len(array)
        m = len(array[0])
        i = n-1
        j = 0
        while i>=0 and j<=m-1: # 关键：从数组的左下角 / 右上角开始找（根据大小比较可以制定不同的动作）
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                i = i-1
            else:
                j = j+1
        return False
