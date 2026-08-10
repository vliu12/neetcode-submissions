class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        # we can determine how many times it was rotated by looking at the first elem
        # 123456
        # 6 - 3 = 3 + 1

        # rotating array 4 times, moves last 4 elems to the beginning

        l = 0
        r = n - 1

        # [3,4,5,6,1,2]
        # 6 1 2 3 4 5
        while l < r:
            mid = (r + l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            
        return nums[l]

        
        

