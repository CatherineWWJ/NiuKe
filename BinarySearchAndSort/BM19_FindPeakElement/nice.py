# @param nums int整型一维数组
# @return int整型
#
class Solution: # 题意：相邻元素值不相等
    def findPeakElement(self , nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # 二分法
        while left < right:
            mid = int((left + right) / 2)
            # 右边是往下，不一定有坡峰
            if nums[mid] > nums[mid+1]:
                right = mid # mid有可能是峰值！！！，必须包含在区间内
            # 右边是往上，一定能找到波峰
            else: # mid必不是峰值！！！，因此不包含在区间内
                left = mid + 1
        # 其中一个波峰
        return right
