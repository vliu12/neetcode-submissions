class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joinList = nums1+nums2
        n = len(joinList)
        joinList.sort()
        if (n % 2 == 0):
            m1 = n//2
            m2 = n//2 - 1
            print(m1,m2)
            med = (joinList[m1] + joinList[m2]) / 2
            return med
        else:
            m = n // 2
            return joinList[m]