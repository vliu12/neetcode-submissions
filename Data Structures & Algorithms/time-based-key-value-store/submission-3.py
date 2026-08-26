class TimeMap:

    def __init__(self):
        self.key_to_time = collections.defaultdict(list) # given key, value, time store key : [value, time]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_time[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        best = 0
        all_values = self.key_to_time[key] # list of value time pairs

        if all_values == []:
            return ""

        l = 0
        r = len(all_values) - 1

        last_val, last_time = all_values[-1]

        while l <= r:
            mid = (r + l) // 2
            curr_val, curr_time = all_values[mid]
            if curr_time == timestamp:
                return curr_val
            elif curr_time < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        if r == -1:
            return ""

        return all_values[r][0]




        
                


        
