# @param a int整型一维数组
# @param n int整型
# @param K int整型
# @return int整型
#
import random
class Solution:
    def partition(self, a: List[int], low: int, high: int, k: int) -> int:
        n = high - low + 1
        x = random.randint(0, 10000)%n+low
        a[low], a[x] = a[x], a[low]
        v = a[low]
        i = low+1
        j = high
        while True:
            while j>=low+1 and a[j]<v: # 较大的值在前
                j -= 1
            while i<=high and a[i]>v: # 较小的值在后
                i += 1
            if i>=j:
                break
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        a[low], a[j] = a[j], a[low] # 最后索引j会停在标杆元素所在的位置（索引为x）
        if j+1 == k:
            return a[j]
        elif j+1<k:
            return self.partition(a, j+1, high, k)
        else:
            return self.partition(a, low, j-1, k)


    def findKth(self , a: List[int], n: int, K: int) -> int:
        res = self.partition(a, 0, n-1, K)
        return res