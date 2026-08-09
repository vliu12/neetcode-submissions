class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = len(temperatures)

        for i in range(n):
            count = 1
            j = i+1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1

            count = 0 if j == n else count
            result.append(count)
        return result
                
                