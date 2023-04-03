# @param numbers int整型一维数组
# @return int整型
#
class Solution:
    def MoreThanHalfNum_Solution(self , numbers: List[int]) -> int:
        res = numbers[0]
        count = 1
        for i in range(1, len(numbers)):
            if res == numbers[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    res = numbers[i]
                    count = 1
        return res
