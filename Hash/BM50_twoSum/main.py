# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
class Solution:
    def twoSum(self , numbers: List[int], target: int) -> List[int]:
        hash = dict()
        for i in range(len(numbers)):
            if target - numbers[i] in hash and hash[target-numbers[i]] != i+1:
                j = hash[target-numbers[i]]
                if i+1<j:
                    return [i+1, j]
                if i+1>j:
                    return [j, i+1]
            hash[numbers[i]] = i+1
