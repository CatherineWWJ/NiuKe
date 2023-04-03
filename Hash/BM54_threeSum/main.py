# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def twosum(self, num: List[int], target: int) -> List[List[int]]:
        res = []
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                if num[i] + num[j] == target:
                    res.append([num[i], num[j]])
        return res

    def threeSum(self , num: List[int]) -> List[List[int]]:
        num.sort()
        ans = []
        for i in range(len(num)):
            if i == 0 or (i-1>=0 and num[i] != num[i-1]):
                res = self.twosum(num[i+1:], 0-num[i])
                if res:
                    for j in range(len(res)):
                        res[j].insert(0, num[i])
                        ans.append(res[j])
        i = 0
        while i+1<len(ans):
            if ans[i] == ans[i+1]:
                ans.pop(i)
            else:
                i += 1
        return ans
