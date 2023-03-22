# @param data int整型一维数组
# @return int整型
#
class Solution:
    mod = 1000000007

    def MergeSort(self, left: int, right: int, data: List[int]) -> int:
        if left >= right:
            return 0
        mid = (left + right) // 2
        res = self.MergeSort(left, mid, data) + self.MergeSort(mid + 1, right, data)
        # 假定此后2个子序列已排序
        i = left
        j = mid + 1
        sum = 0
        temp = []
        while j < right + 1:
            while data[i] <= data[j] and i <= mid:
                temp.append(data[i])
                i += 1
            temp.append(data[j])
            sum += mid - i + 1
            j += 1
        while i <= mid:
            temp.append(data[i])
            i += 1
        data[left:right + 1] = temp # 排序
        return res + sum # 逆序数累加

    def InversePairs(self, data: List[int]) -> int:
        n = len(data)
        l = 0
        r = n - 1
        return self.MergeSort(l, r, data) % self.mod
