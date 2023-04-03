# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def minNumberDisappeared(self , nums: List[int]) -> int:
        n = len(nums)
        hash = [False]*n
        for i in range(n):
            if 0<nums[i]<=n:
                hash[nums[i]-1] = True
        for i in range(n):
            if not hash[i]:
                return i+1
        return n+1
    