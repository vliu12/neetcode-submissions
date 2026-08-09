class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        newNums = sorted(set(nums))
        
        counter = 1

        ult = 1

        for i in range(1, len(newNums)):
            if newNums[i]== newNums[i - 1] + 1:
                counter += 1
                ult = max(ult, counter)
            else:
                counter = 1

        return ult
            

