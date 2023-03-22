# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def findPeakElement(self , nums: List[int]) -> int: # 思想：找峰值就是找尽可能大的元素
        # write code here
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0]>nums[1] else 1
        l = 0
        r = len(nums)-1
        # 确定峰值：比较相邻左右元素大小
        while l<r:
            mid = (l+r) // 2
            if nums[mid-1]<nums[mid]<nums[mid+1]: # 情况1：严格递增（右半段）
                l = mid+1
            elif nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]: # 情况2：mid在局部最高点（峰值）
                return mid
            elif nums[mid-1]>nums[mid]>nums[mid+1]: # 情况3：严格递减（左半段）
                r = mid-1
            else: # 情况4：mid在局部最低点（不确定峰值的位置，逐个缩减区间）
                r = r-1
        return l
