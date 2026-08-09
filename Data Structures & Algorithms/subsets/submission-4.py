class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current_subset):
            # Add the current_subset to the result (base case for each valid subset)
            result.append(list(current_subset)) 

            # Explore choices for remaining elements
            for i in range(start, len(nums)):
                # Include the current element
                current_subset.append(nums[i])
                # Recursively call backtrack for the next elements
                backtrack(i + 1, current_subset)
                # Backtrack: remove the last added element to explore other paths
                current_subset.pop()

        # Initiate the backtracking process with an empty subset starting from index 0
        backtrack(0, [])
        return result
        
