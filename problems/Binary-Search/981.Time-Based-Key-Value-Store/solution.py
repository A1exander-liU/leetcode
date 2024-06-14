class TimeMap:
    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = {"timestamps": [timestamp], timestamp: value}
        else:
            self.keys[key]["timestamps"].append(timestamp)
            self.keys[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""

        timestamps = self.keys[key]["timestamps"]

        left = 0
        right = len(timestamps) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if timestamps[mid] == timestamp:
                return self.keys[key][timestamps[mid]]
            elif timestamps[mid] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return "" if right == -1 else self.keys[key][timestamps[right]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
