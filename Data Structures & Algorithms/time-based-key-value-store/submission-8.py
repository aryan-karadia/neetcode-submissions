from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # dictionary
        self.timeMap[key].append([value, timestamp])
        return None

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key]
        if len(values) == 0:
            return ""
        l, r = 0, len(values) - 1
        # if exists
        target = timestamp
        while True:
            while l <= r:
                mid = (l + r) // 2
                if values[mid][1] == target:
                    return values[mid][0]

                # is it greater or less?
                if target > values[mid][1]:
                    l = mid + 1
                else:
                    r = mid - 1
                
            # reset l, r
            l, r = 0, len(values) - 1
            # move target to most recent timestamp
            prev_timestamp = None
            for _, x in values:
                if x < timestamp:
                    prev_timestamp = x

            if prev_timestamp is None:
                return ""
            target = prev_timestamp 
        
