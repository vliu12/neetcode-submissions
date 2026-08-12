class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binSearch(arr, target):
            l = 0
            r = len(arr) - 1

            while l < r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            
            return arr[l] == target


        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
           first = matrix[row][0]
           last = matrix[row][cols-1]
           if target >= first and target <= last:
                return binSearch(matrix[row], target)

        return False
                