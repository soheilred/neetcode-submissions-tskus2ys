class TimeMap:

    def __init__(self):
        self.tmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = OrderedDict()
        # else:
        self.tmap[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.tmap:
            if timestamp in self.tmap[key]:
                return self.tmap[key][timestamp]
            else:
                minT = min(self.tmap[key])
                if timestamp < minT:
                    return ""
                # perform a bst to find the right timestamp
                # maxT = max(self.tmap[key])
                res = self.tmap[key][minT]
                for t in self.tmap[key]:
                    if t > timestamp:
                        return res
                    res = self.tmap[key][t]
                return res
        
        else:
            return ""
        
