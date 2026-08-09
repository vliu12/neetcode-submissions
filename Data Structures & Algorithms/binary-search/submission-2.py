class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 

        r = len(nums) - 1

        while l <= r:
            
            mid = l + ((r - l) // 2)

            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                print("target is less")
                r = mid - 1

            else:
                l = mid + 1
                print("target is more")

        return -1


        
        