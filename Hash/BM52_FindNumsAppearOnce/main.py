# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindNumsAppearOnce(self , array: List[int]) -> List[int]:
        eor = 0
        for i in range(len(array)):
            eor ^= array[i]
        lastTag = eor & (~eor + 1)
        num1 = 0
        for i in range(len(array)):
            if array[i] & lastTag:
                num1 ^= array[i]
        num2 = eor ^ num1
        if num1<num2:
            return [num1, num2]
        else:
            return [num2, num1]
