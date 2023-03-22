# @param rotateArray int整型一维数组
# @return int整型
#
class Solution:
    def minNumberInRotateArray(self , rotateArray: List[int]) -> int:
        l = 0
        r = len(rotateArray)-1
        while l<=r:
            mid = (l+r) // 2
            if rotateArray[mid] > rotateArray[r]: # 必有旋转：最小的数字一定在中点右边（不包含中点）
                l = mid+1
            elif rotateArray[mid] < rotateArray[r]: # 不一定旋转：最小的数字一定在中点 / 中点左边
                r = mid
            else: # 此时无法判断最小值的位置，只能逐个缩减右界！！！
                r = r-1
        return rotateArray[l]
