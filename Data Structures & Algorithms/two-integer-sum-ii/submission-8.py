class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # constraint is no additional space

        def binsearch(wanted, start):
            l = start
            r = len(numbers) - 1

            while l <= r:
                mid = (r + l)//2
                if numbers[mid] == wanted:
                    return mid
                elif numbers[mid] < wanted:
                    l = mid + 1
                else:
                    r = mid - 1

            return -1

        n = len(numbers)

        for i in range(n):
            left = numbers[i]
            to_search = target - left
            right = binsearch(to_search, i + 1)
            
            if right != -1:
                return [i + 1, right + 1]

        return []


        
        