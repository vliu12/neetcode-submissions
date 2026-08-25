class Solution:
    # we only want to consider start points where like the next elem is i + 1
    # or we could consider points that are non - consecutive
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        set_nums = set(nums)
        best_length = 0

        # nums = [2,20,4,10,3,4,5]
        for num in nums:
            # this is like a start index, we know there isnt a smaller start
            if (num - 1) not in set_nums:
                count = 1 # starting length
                next_num = num + 1 # next number we're looking for
                while next_num in set_nums: # while the next number exists
                    count += 1
                    next_num += 1
                
                best_length = max(count, best_length)

        return best_length
        


        
            

