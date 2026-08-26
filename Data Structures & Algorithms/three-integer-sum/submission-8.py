class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []

        # [-1,0,1,2,-1,-4]

        # [-4, -1, -1, 0, 1, 2]

        # so we can keep two pointers
        # we want the sum of our 2 pointers to end up being like -nums[k] = nums[j] + nums[i]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                target = -(nums[k] + nums[j])
                if nums[i] == target:
                    out.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif target < nums[i]:
                    k -= 1
                else:
                    j += 1

        return out

            

            

            

            


