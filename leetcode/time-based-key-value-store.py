class TimeMap:

    def __init__(self):

        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
   

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            arr = self.store[key]
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = (l + r) // 2
                mid_timestamp, mid_value = arr[mid]

                if mid_timestamp == timestamp:
                    return mid_value
                elif mid_timestamp < timestamp:
                    l = mid + 1
                else:
                    r = mid - 1

            if r >= 0:
                return arr[r][1]

        return ""





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)