# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def minNumberDisappeared(self , nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i]>n:
                nums[i] = n+1
        for i in range(n):
            if 0<abs(nums[i])<=n: # 注意：这里是绝对值大小（前面该位置对应的正整数存在将其变为负数）
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1 # 不存在缺失的正整数
    